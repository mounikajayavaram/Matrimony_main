# Generated by Django 4.2.1 on 2023-05-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.CharField(default='2023-05-09', max_length=10),
        ),
    ]