from django.shortcuts import render
from problems.models import Problem, Category
from django.db.models import Count


def problems_view(request):
    problems = Problem.objects.all().annotate(Count('categories'))
    categories = Category.objects.all()

    category_pk = request.GET.get('category')
    if category_pk is not None and category_pk != '0':
        problems = problems.filter(categories__pk=category_pk)

    return render(request, "problems/index.html",
                  context={'problems': problems,
                           'categories': categories
                           })
