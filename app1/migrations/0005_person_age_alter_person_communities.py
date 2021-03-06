# Generated by Django 4.0.1 on 2022-01-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_sex_person_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='communities',
            field=models.ManyToManyField(blank=True, to='app1.Community'),
        ),
    ]
