# Generated by Django 5.1 on 2024-11-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='prn',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
