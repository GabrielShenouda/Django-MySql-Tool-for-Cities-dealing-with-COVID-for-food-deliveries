# Generated by Django 3.0.3 on 2020-05-08 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdresseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=50)),
                ('departement', models.CharField(choices=[('1', 'Ain'), ('2', 'Aisne'), ('3', 'Allier'), ('75', 'Paris'), ('78', 'Yvelines'), ('91', 'Essonne'), ('92', 'Hauts-de-Seine'), ('93', 'Seine-Saint-Denis'), ('94', 'Val-de-Marne'), ('95', "Val d'Oise")], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'adresseUser',
                'ordering': ['departement'],
            },
        ),
    ]
