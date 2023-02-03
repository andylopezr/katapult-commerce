# Generated by Django 4.1.5 on 2023-02-03 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(choices=[('AVV', 'AV Villas'), ('BDB', 'Banco de Bogota'), ('BCO', 'Bancolombia'), ('BBV', 'BBVA'), ('BDO', 'Banco de Occidente'), ('BDO', 'Davivienda'), ('CSO', 'Caja Social'), ('ITA', 'Itaú'), ('SCO', 'Scotiabank'), ('POP', 'Popular')], default='AVV', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=255)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bank.bank')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]