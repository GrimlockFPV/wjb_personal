# Generated by Django 3.2.6 on 2021-08-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210823_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured',
            field=models.IntegerField(blank=True, choices=[(0, 'Primary'), (1, 'Secondary')]),
        ),
    ]
