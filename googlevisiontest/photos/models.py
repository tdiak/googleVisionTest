# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


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
        (1, 'Joy'),
        (2, 'Sorrow'),
        (3, 'Anger'),
        (4, 'Surprise')
    )
    photo = models.ForeignKey(
        Photo,
        verbose_name="Photo"
    )
    emotion_type = models.PositiveSmallIntegerField(
        verbose_name="Emotion type",
        choices=EMOTIONS
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