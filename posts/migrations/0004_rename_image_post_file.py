# Generated by Django 4.0.5 on 2022-08-17 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='file',
        ),
    ]
