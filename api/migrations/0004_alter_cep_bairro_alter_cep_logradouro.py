# Generated by Django 4.1.6 on 2023-02-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_estado_delete_cepslojacorr_cep_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cep',
            name='bairro',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cep',
            name='logradouro',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
