# Generated by Django 3.1.3 on 2020-11-23 19:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0005_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksIssued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(default=datetime.date(2020, 11, 23))),
                ('return_date', models.DateField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmgmt.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmgmt.user')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(through='libmgmt.BooksIssued', to='libmgmt.User'),
        ),
    ]