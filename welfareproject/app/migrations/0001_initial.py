# Generated by Django 2.2.4 on 2020-04-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userregistrationmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('contactno', models.IntegerField(unique=True)),
                ('companyname', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
