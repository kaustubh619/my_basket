# Generated by Django 2.2.10 on 2020-10-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
    ]
