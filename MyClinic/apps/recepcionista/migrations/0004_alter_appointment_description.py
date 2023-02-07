# Generated by Django 4.1.5 on 2023-02-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recepcionista", "0003_alter_appointment_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="description",
            field=models.CharField(
                choices=[
                    ("Retorno", "Retorno"),
                    ("Exame", "Exame"),
                    ("Consulta", "Consulta"),
                    ("Consulta e Exame", "Consulta e Exame"),
                ],
                default="----------",
                max_length=20,
            ),
        ),
    ]
