# Generated by Django 4.2.1 on 2023-05-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contackdetailsapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Name',
            field=models.CharField(default='null', max_length=62322222222222222),
        ),
    ]