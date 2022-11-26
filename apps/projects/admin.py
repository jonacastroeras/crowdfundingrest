from django.contrib import admin

# Register your models here.
from apps.projects.models import Project, Category, Donant


class DonantsInline(admin.TabularInline):
    model = Donant


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    list_filter = ("category",)
    inlines = (DonantsInline,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Donant)
class DonantAdmin(admin.ModelAdmin):
    pass
