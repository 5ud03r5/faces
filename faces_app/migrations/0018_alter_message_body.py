# Generated by Django 3.2.8 on 2021-11-16 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faces_app', '0017_alter_post_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.CharField(max_length=2083, null=True),
        ),
    ]
