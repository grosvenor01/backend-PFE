# Generated by Django 4.1.5 on 2023-01-27 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='type',
            field=models.CharField(choices=[('theme', 'theme'), ('question', 'question')], default='theme', max_length=10),
        ),
    ]
