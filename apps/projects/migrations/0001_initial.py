# Generated by Django 4.1.3 on 2022-11-18 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        max_length=50, verbose_name="Nombre de la Categoría"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Descripción del Proyecto"),
                ),
            ],
            options={
                "verbose_name": "Categoría",
                "verbose_name_plural": "Categorías",
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Nombre del Proyecto"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Descripción del Proyecto"),
                ),
                ("price", models.FloatField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projectcategory",
                        to="projects.category",
                        verbose_name="Categoría",
                    ),
                ),
            ],
            options={
                "verbose_name": "Proyecto",
                "verbose_name_plural": "Proyectos",
            },
        ),
        migrations.CreateModel(
            name="Donant",
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
                ("name", models.CharField(max_length=150, verbose_name="Donante")),
                ("amount", models.FloatField()),
                ("visible", models.BooleanField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="donantproject",
                        to="projects.project",
                        verbose_name="Proyecto",
                    ),
                ),
            ],
            options={
                "verbose_name": "Donante",
                "verbose_name_plural": "Donantes",
            },
        ),
    ]