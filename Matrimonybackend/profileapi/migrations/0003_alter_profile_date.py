# Generated by Django 4.2.1 on 2023-05-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapi', '0002_alter_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.CharField(default='2023-05-12', max_length=10),
        ),
    ]