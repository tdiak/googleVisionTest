# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.PositiveSmallIntegerField(verbose_name='Red')),
                ('blue', models.PositiveSmallIntegerField(verbose_name='Blue')),
                ('green', models.PositiveSmallIntegerField(verbose_name='Green')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion_type',
                 models.PositiveSmallIntegerField(choices=[(1, 'Joy'), (2, 'Sorrow'), (3, 'Anger'), (4, 'Surprise')],
                                                  verbose_name='Emotion type')),
                ('result', models.CharField(max_length=120, verbose_name='Result')),
            ],
            options={
                'verbose_name': 'Emotion',
                'verbose_name_plural': 'Emotions',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, verbose_name='Label')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=120, verbose_name='Filename')),
                ('file', models.ImageField(upload_to='photos', verbose_name='Image file')),
                ('is_checked', models.BooleanField(default=False, verbose_name='Is checked by vision')),
                ('last_checked_date', models.DateTimeField(blank=True, null=True, verbose_name='Last checked date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.AddField(
            model_name='label',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo',
                                    verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='emotion',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo',
                                    verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='color',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo',
                                    verbose_name='Photo'),
        ),
    ]
