# Generated by Django 5.0.1 on 2024-02-05 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_calificacion_calificaciones_calificaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calificaciones',
            old_name='calificaciones',
            new_name='calificacion',
        ),
    ]
