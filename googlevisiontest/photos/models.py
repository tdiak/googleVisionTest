# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import models
from django.utils.six import python_2_unicode_compatible

from utils.vision_service import VisioService


@python_2_unicode_compatible
class Photo(models.Model):
    filename = models.CharField(
        verbose_name="Filename",
        max_length=120
    )
    file = models.ImageField(
        verbose_name="Image file",
        upload_to='photos'
    )
    is_checked = models.BooleanField(
        verbose_name = "Is checked by vision",
        default=False
    )
    last_checked_date = models.DateTimeField(
        verbose_name="Last checked date",
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(
        verbose_name="Is deleted",
        default=False
    )

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.filename

    def save_colors(self, colors):
        for color in colors:
            Color(
                photo=self,
                red=color[0],
                green=color[1],
                blue=color[2]
            ).save()

    def save_labels(self, labels):
        for label in labels:
            Label(
                photo=self,
                label=label
            ).save()

    def save_emotions(self, faces):
        for face in faces:
            for key, emotion in face.iteritems():
                Emotion(
                    photo=self,
                    emotion_type=key,
                    result=emotion.value
                ).save()

    def use_vision(self):
        path = '{0}{1}'.format(settings.MEDIA_ROOT, self.file.url.split('media')[1])
        vision_service = VisioService(path)
        vision_service.initialize()
        data = vision_service.get_info()
        self.save_colors(data['colors'])
        self.save_labels(data['labels'])
        self.save_emotions(data['faces'])
        self.last_checked_date = datetime.datetime.now()
        self.is_checked = True

    def save(self, use_vision=False, *args, **kwargs):
        super(self.__class__, self).save(*args, **kwargs)
        if use_vision or not self.is_checked:
            print 'test'
            Color.objects.filter(photo=self).delete()
            Label.objects.filter(photo=self).delete()
            Emotion.objects.filter(photo=self).delete()
            self.use_vision()
            super(self.__class__, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Color(models.Model):
    photo = models.ForeignKey(
        Photo,
        verbose_name="Photo"
    )
    red = models.PositiveSmallIntegerField(
        verbose_name="Red"
    )
    blue = models.PositiveSmallIntegerField(
        verbose_name="Blue"
    )
    green = models.PositiveSmallIntegerField(
        verbose_name="Green"
    )

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return "({0}, {1}, {2})".format(self.red, self.green, self.blue)


@python_2_unicode_compatible
class Label(models.Model):
    photo = models.ForeignKey(
        Photo,
        verbose_name="Photo"
    )
    label = models.CharField(
        verbose_name="Label",
        max_length=255
    )

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = "Labels"

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class Emotion(models.Model):
    EMOTIONS = (
        ('joy', 'Joy'),
        ('sorrow', 'Sorrow'),
        ('anger', 'Anger'),
        ('surprise', 'Surprise')
    )
    photo = models.ForeignKey(
        Photo,
        verbose_name="Photo"
    )
    emotion_type = models.CharField(
        verbose_name="Emotion type",
        choices=EMOTIONS,
        max_length=12
    )
    result = models.CharField(
        verbose_name="Result",
        max_length=120
    )

    class Meta:
        verbose_name = "Emotion"
        verbose_name_plural = "Emotions"

    def __str__(self):
        return "{0} - {1}".format(self.get_emotion_type_display(), self.result)