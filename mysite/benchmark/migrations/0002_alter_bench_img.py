# Generated by Django 4.1.5 on 2023-02-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bench',
            name='img',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
