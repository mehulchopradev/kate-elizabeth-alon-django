# Generated by Django 3.1.3 on 2020-11-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('country', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]