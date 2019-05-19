# Generated by Django 2.2 on 2019-05-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('DOB', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Appusers',
            },
        ),
    ]