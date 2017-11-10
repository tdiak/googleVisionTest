# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Photo, Label, Emotion, Color


class LabelInline(admin.TabularInline):
    model = Label


class EmotionInline(admin.TabularInline):
    model = Emotion


class ColorInline(admin.TabularInline):
    model = Color


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [
        LabelInline,
        ColorInline,
        EmotionInline
    ]
    list_display = (
        'filename',
        'is_deleted',
        'is_checked'
    )