# Generated by Django 3.1.3 on 2020-12-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raterapi', '0004_auto_20201205_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]