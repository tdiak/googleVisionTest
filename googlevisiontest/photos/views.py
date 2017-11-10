# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets

from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.filter(is_deleted=False)
    serializer_class = PhotoSerializer