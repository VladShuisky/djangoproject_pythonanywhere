# Generated by Django 4.0.1 on 2022-01-26 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 6, 55, 27, 353690, tzinfo=utc)),
        ),
    ]
