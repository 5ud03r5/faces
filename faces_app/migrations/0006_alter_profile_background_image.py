# Generated by Django 3.2.8 on 2021-11-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faces_app', '0005_auto_20211111_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(default='default_background.jpg', upload_to=''),
        ),
    ]