# Generated by Django 3.2.5 on 2022-05-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_lastface_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userface',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
