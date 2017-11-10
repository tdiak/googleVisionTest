# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import io

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from google.cloud import vision


class Command(BaseCommand):
    help = 'Send test request'
    vision_client = vision.Client(settings.API_KEY_PATH)

    def handle(self, *args, **options):
        file_name = os.path.join(settings.BASE_DIR, 'google', 'test.png')

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            image = self.vision_client.image(
                content=content)

        labels = image.detect_labels()

        print('Labels:')
        for label in labels:
            print(label.description)
