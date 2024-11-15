# Generated by Django 5.1 on 2024-11-12 01:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emergencias', '0002_alter_servicio_unidad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='bombero_reporta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_reporta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='piloto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_piloto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='telefonista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_telefonista', to=settings.AUTH_USER_MODEL),
        ),
    ]
