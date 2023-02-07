# Generated by Django 4.1.5 on 2023-02-05 00:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recepcionista", "0002_rename_recepcionist_appointment_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="description",
            field=models.CharField(
                choices=[
                    ("Retorno", "Retorno"),
                    ("Consulta", "Consulta"),
                    ("Exame", "Exame"),
                    ("Consulta e Exame", "Consulta e Exame"),
                ],
                default="----------",
                max_length=20,
            ),
        ),
    ]