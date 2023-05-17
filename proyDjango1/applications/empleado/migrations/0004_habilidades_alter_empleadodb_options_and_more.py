# Generated by Django 4.2 on 2023-05-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empleado", "0003_empleadodb_departamento_empleadodb_empleo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Habilidades",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "habilidad",
                    models.CharField(max_length=50, verbose_name="Habilidad"),
                ),
            ],
            options={
                "verbose_name": "Habilidad",
                "verbose_name_plural": "Habilidades de los empleados",
            },
        ),
        migrations.AlterModelOptions(
            name="empleadodb",
            options={
                "ordering": ["apellido"],
                "verbose_name": "Empleado",
                "verbose_name_plural": "Empleados de la empresa",
            },
        ),
        migrations.AlterUniqueTogether(
            name="empleadodb", unique_together={("nombre", "apellido")},
        ),
    ]