# Generated by Django 2.2.4 on 2020-04-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thoughtsmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_usernmae', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('t_contno', models.IntegerField(unique=True)),
            ],
        ),
    ]
