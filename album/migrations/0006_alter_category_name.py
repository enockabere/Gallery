# Generated by Django 3.2.7 on 2021-09-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_rename_place_image_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]