# Generated by Django 5.1.4 on 2025-01-15 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mutual_funds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mutualfund',
            options={'verbose_name_plural': 'Mutual Funds'},
        ),
        migrations.AlterField(
            model_name='mutualfund',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='mutualfund',
            name='symbol',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='mutualfund',
            unique_together={('name', 'symbol')},
        ),
    ]
