# Generated by Django 4.0.1 on 2022-02-08 09:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 9, 22, 54, 972022, tzinfo=utc)),
        ),
    ]
