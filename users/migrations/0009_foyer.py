# Generated by Django 3.0.3 on 2020-05-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200509_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Foyer',
            },
        ),
    ]
