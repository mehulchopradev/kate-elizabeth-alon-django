# Generated by Django 3.1.3 on 2020-11-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0002_auto_20201119_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.FloatField(blank=True, null=True)),
                ('pages', models.IntegerField()),
                ('published_date', models.DateField(blank=True, null=True)),
                ('no_of_copies', models.IntegerField()),
            ],
        ),
    ]
