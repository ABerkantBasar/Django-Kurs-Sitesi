# Generated by Django 4.1.2 on 2022-12-24 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_video_alter_category_slug_alter_course_slug_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]