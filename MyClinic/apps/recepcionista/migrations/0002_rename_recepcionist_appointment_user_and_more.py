# Generated by Django 4.1.5 on 2023-01-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recepcionista", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointment",
            old_name="recepcionist",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="appointment",
            name="description",
            field=models.CharField(
                choices=[
                    ("Exame", "Exame"),
                    ("Retorno", "Retorno"),
                    ("Consulta e Exame", "Consulta e Exame"),
                    ("Consulta", "Consulta"),
                ],
                default="----------",
                max_length=20,
            ),
        ),
    ]
