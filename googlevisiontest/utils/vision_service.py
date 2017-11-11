# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io

from django.conf import settings
from google.cloud import vision


class VisioService(object):
    vision_client = vision.Client(settings.API_KEY_PATH)

    def __init__(self, image_path, auth_key=None):
        if auth_key:
            self.vision_client = vision.Client(settings.API_KEY_PATH)

        self.image_path = image_path

    def __get_labels(self):
        labels = self.image_data.detect_labels()
        return [label.description for label in labels]

    def __get_colors(self):
        colors = self.image_data.detect_properties().colors
        return [(color.color.red, color.color.green, color.color.blue) for color in colors]

    def __get_faces(self):
        faces = self.image_data.detect_faces()
        emotions = []
        for face in faces:
            temp = {
                'joy': face.emotions.joy,
                'sorrow': face.emotions.sorrow,
                'anger': face.emotions.anger,
                'surprise': face.emotions.surprise
            }
            emotions.append(temp)
        return emotions

    def initialize(self):
        with io.open(self.image_path, 'rb') as image_file:
            content = image_file.read()
            self.image_data = self.vision_client.image(
                content=content)

    def get_info(self):
        return {
            'labels': self.__get_labels(),
            'colors': self.__get_colors(),
            'faces': self.__get_faces()
        }
