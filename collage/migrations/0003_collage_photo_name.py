# Generated by Django 3.1.3 on 2020-12-18 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collage', '0002_auto_20201218_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='collage',
            name='photo_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]