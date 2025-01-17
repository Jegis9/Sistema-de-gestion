# Generated by Django 5.1 on 2024-10-17 17:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('stock_inicial', models.IntegerField(default=0)),
                ('stock_actual', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='InsumoLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadTomada', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='Administrativo.insumos')),
            ],
        ),
    ]
