# Generated by Django 3.2.6 on 2021-08-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210824_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured',
        ),
        migrations.AddField(
            model_name='post',
            name='featured_primary',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='featured_secondary',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
