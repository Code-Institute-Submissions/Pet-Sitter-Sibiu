# Generated by Django 3.1.7 on 2021-03-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20210331_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Bad'), (2, 'Not Good'), (3, 'Ok'), (4, 'Good'), (5, 'Amazing')], default=1),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='review',
            field=models.TextField(),
        ),
    ]