# Generated by Django 4.0.5 on 2022-08-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='uploads'),
        ),
    ]