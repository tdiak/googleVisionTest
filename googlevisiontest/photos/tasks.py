from __future__ import absolute_import, unicode_literals
from celery import shared_task

from utils.vision_save_manager import VisionSaveManager


@shared_task()
def detect(pk):
    from photos.models import Photo
    obj = Photo.objects.get(pk=pk)
    VisionSaveManager(obj=obj).run()
