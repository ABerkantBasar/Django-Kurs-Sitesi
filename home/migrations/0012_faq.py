# Generated by Django 4.1.2 on 2022-12-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=255)),
                ('answer', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayir')], max_length=10)),
                ('crate_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
