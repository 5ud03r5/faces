# Generated by Django 3.2.8 on 2021-11-16 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faces_app', '0016_post_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_creator', to='faces_app.profile'),
        ),
    ]
