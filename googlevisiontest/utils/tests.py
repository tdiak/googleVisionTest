# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.test import TestCase

from utils.vision_save_manager import VisionSaveManager


class VisionManagerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.vision_data = VisionSaveManager().run(path=settings.API_TEST_IMAGE_PATH, commit=False)

    def test_colors(self):
        self.assertIsInstance(self.vision_data['colors'], list)

    def test_labels(self):
        self.assertIsInstance(self.vision_data['labels'], list)

    def test_emotions(self):
        self.assertIsInstance(self.vision_data['faces'], list)