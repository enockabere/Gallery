# Generated by Django 3.2.7 on 2021-09-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0008_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]