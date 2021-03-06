# Generated by Django 3.0.3 on 2020-05-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Fruits et Légumes', 'Fruits et Légumes'), ('Viandes et Poissons', 'Viandes et Poissons'), ('Féculents', 'Féculents'), ('Produits laitiers', 'Produits laitiers'), ('Pâtisseries et Desserts', 'Pâtisseries et Desserts'), ('Snacks', 'Snacks'), ('Sauces et Condiments', 'Sauces et Condiments'), ('Hygiène', 'Hygiène'), ("Produits d'entretiens", "Produits d'entretiens"), ('Informatique', 'Informatique'), ('Médicaments en Vente libre', 'Médicaments en Vente libre'), ('Paniers Repas', 'Paniers Repas'), ('Autre', 'Autre')], max_length=100)),
                ('restriction', models.CharField(choices=[('Viande', 'Viande'), ('Gluten', 'Gluten'), ('Lactose', 'Lactose'), ('Fruits secs', 'Fruits secs')], max_length=100)),
                ('prix', models.FloatField()),
                ('quantite', models.CharField(choices=[('500 g', '500 g'), ('1 L', '1 L'), ('6', '6'), ('100 g', '100 g'), ('100 mL', '100 mL')], max_length=50)),
            ],
            options={
                'verbose_name': 'Produit',
                'ordering': ['nom'],
            },
        ),
    ]
