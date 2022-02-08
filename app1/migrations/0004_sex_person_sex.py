# Generated by Django 4.0.1 on 2022-01-18 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_person_communities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.sex'),
        ),
    ]