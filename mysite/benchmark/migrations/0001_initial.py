# Generated by Django 4.1.5 on 2023-02-07 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bench',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=None, upload_to='')),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField()),
                ('seclusion', models.IntegerField()),
                ('accesibility', models.IntegerField()),
                ('squirrels', models.IntegerField()),
                ('time_submitted', models.TimeField(default=None)),
                ('time_spent', models.IntegerField(default=None)),
                ('rating', models.IntegerField()),
                ('bench', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benchmark.bench')),
            ],
        ),
    ]
