from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la Categoría")
    description = models.TextField(verbose_name="Descripción del Proyecto")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre del Proyecto")
    description = models.TextField(verbose_name="Descripción del Proyecto")
    price = models.FloatField()
    image = models.ImageField(verbose_name="Imagen de Consulta", blank=False, null=True, upload_to="fogon")
    category = models.ForeignKey(Category, verbose_name="Categoría", related_name="projectcategory",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.name


class Donant(models.Model):
    name = models.CharField(max_length=150, verbose_name="Donante")
    amount = models.FloatField()
    visible = models.BooleanField()
    project = models.ForeignKey(Project, verbose_name="Proyecto", related_name="donantproject",
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Donante"
        verbose_name_plural = "Donantes"

    def __str__(self):
        return self.name
