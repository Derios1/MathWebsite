from django.shortcuts import render
from django.contrib.auth import get_user
from problems.models import Problem, Category
from django.db.models import Count
from Parser.parser import Parser


def problems_view(request):
    problems = Problem.objects.all().annotate(Count('categories'))
    categories = Category.objects.all()

    if request.method == "POST":
        checked_categories = list(map(int, request.POST.getlist('categories')))
        if len(checked_categories):
            problems = problems.filter(categories__pk__in=checked_categories)

    return render(request, "problems/index.html",
                  context={'problems': problems,
                           'categories': categories
                           })


def problem_page_view(request, id):
    problem = Problem.objects.get(pk=id)
    user = get_user(request)
    answer_status = -1
    text = ''

    if user.is_authenticated and problem in user.profile.solved_problems.all():
        answer_status = True

    if request.method == "POST":
        text = request.POST["formula"]

        input_answer = Parser(text, problem.symbols)
        answer = Parser(problem.answer, problem.symbols)
        answer_status = input_answer == answer
        if answer_status and user.is_authenticated:
            user.profile.solved_problems.add(problem)
            user.save()
            user.profile.save()

    return render(request, "problems/problem-page.html",
                  context={'problem': problem, 'answer_status': answer_status, 'prev_text': text})
