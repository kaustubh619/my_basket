# Generated by Django 2.2.10 on 2020-10-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201016_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='thumbnail',
            field=models.ImageField(upload_to='category_thumbnails'),
        ),
    ]