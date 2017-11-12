# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings

from utils.vision_service import VisioService


class VisionSaveManager(object):
    def __init__(self, obj=None):
        self.obj = obj
        self.data = None

    def __save_colors(self, colors):
        for color in colors:
            from photos.models import Color
            self.__clear(Color)
            Color(
                photo=self.obj,
                red=color[0],
                green=color[1],
                blue=color[2]
            ).save()

    def __save_labels(self, labels):
        from photos.models import Label
        self.__clear(Label)
        for label in labels:
            Label(
                photo=self.obj,
                label=label
            ).save()

    def __save_emotions(self, faces):
        from photos.models import Emotion
        self.__clear(Emotion)
        for face in faces:
            for key, emotion in face.iteritems():
                Emotion(
                    photo=self.obj,
                    emotion_type=key,
                    result=emotion.value
                ).save()

    def __clear(self, class_name):
        class_name.objects.filter(photo=self.obj).delete()

    def __save_data(self, data):
        self.__save_colors(data['colors'])
        self.__save_labels(data['labels'])
        self.__save_emotions(data['faces'])

    def run(self, path=None, commit=True):
        if not path:
            path = '{0}{1}'.format(settings.MEDIA_ROOT, self.obj.file.url.split('media')[1])
        vision_service = VisioService(path)
        vision_service.initialize()
        self.data = vision_service.get_info()
        if commit:
            self.__save_data(self.data)
            self.obj.last_checked_date = datetime.datetime.now()
            self.obj.is_checked = True
            self.obj.save()

        return self.data
