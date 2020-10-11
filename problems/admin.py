from django.contrib import admin
from problems.models import Problem, Category


@admin.register(Problem)
class AdminProblem(admin.ModelAdmin):
    pass


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass

