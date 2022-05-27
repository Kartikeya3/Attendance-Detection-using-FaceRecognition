# Generated by Django 4.0.4 on 2022-05-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_attendence_studentface'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_face', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('date', models.DateField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('ranking', models.IntegerField()),
                ('profession', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('employee', 'Employee'), ('visitor', 'Student')], default='employee', max_length=20, null=True)),
                ('present', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shift', models.TimeField()),
            ],
        ),
    ]