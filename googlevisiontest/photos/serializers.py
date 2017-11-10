# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from models import Photo, Label, Emotion, Color


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('label',)


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('emotion_type', 'result',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('red', 'blue', 'green',)


class PhotoSerializer(serializers.ModelSerializer):
    label_set = LabelSerializer(many=True, read_only=True)
    emotion_set = EmotionSerializer(many=True, read_only=True)
    color_set = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'filename', 'file', 'label_set', 'emotion_set', 'color_set')