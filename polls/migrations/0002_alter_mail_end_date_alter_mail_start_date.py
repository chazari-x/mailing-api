# Generated by Django 5.0.5 on 2024-05-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='end_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mail',
            name='start_date',
            field=models.IntegerField(),
        ),
    ]