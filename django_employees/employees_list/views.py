from django.shortcuts import render
from .models import *


def employees_list(request):
    context = {'deps': {}}
    deps = Department.objects.all().filter(head_department=None)
    for item in deps:
        context['deps'].update(take_deps_recursive(item))
    return render(request, 'index.html', context)


def take_deps_recursive(item=None):
    context = {item: {}}
    deps = Department.objects.all().filter(head_department=item.id)
    if not deps:
        context[item] = list(Employee.objects.all().filter(department=item.id))
    else:
        for dep in deps:
            context[item].update(take_deps_recursive(dep))
    return context
