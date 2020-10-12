from django.contrib import admin
from problems.models import Problem, Category


@admin.register(Problem)
class AdminProblem(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title']

