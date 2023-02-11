# Generated by Django 4.1.5 on 2023-02-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recepcionista", "0009_income_type_income_alter_appointment_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="description",
            field=models.CharField(
                choices=[
                    ("Retorno", "Retorno"),
                    ("Consulta", "Consulta"),
                    ("Consulta e Exame", "Consulta e Exame"),
                ],
                default="----------",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="income",
            name="type_income",
            field=models.CharField(
                choices=[
                    ("Consulta", "Consulta"),
                    ("Exame", "Exame"),
                    ("Consulta e Exame", "Consulta e Exame"),
                ],
                default="----------",
                max_length=20,
            ),
        ),
    ]
