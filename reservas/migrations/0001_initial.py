# Generated by Django 4.2.5 on 2023-09-21 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao_tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_occup', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto_Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_Quarto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quartos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_Quarto', models.IntegerField(default=0)),
                ('fktipo_Quarto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservas.quarto_cat')),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ini', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.cliente')),
                ('fk_quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.quartos')),
                ('fk_tipooccup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservas.ocupacao_tipo')),
            ],
        ),
    ]
