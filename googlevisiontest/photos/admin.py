# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Photo, Label, Emotion, Color
from photos.tasks import detect


def detect_image(modeladmin, request, queryset):
    for item in queryset:
        detect.delay(pk=item.pk)


detect_image.short_description = "Detect once again"


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

    actions = (
        detect_image,
    )
