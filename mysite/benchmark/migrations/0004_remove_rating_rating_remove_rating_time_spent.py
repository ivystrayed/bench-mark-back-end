# Generated by Django 4.1.5 on 2023-02-14 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0003_alter_bench_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='time_spent',
        ),
    ]
