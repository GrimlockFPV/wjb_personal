# Generated by Django 3.2.6 on 2021-08-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210825_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured',
            field=models.CharField(blank=True, choices=[('P', 'Primary'), ('S', 'Secondary')], max_length=1),
        ),
    ]
