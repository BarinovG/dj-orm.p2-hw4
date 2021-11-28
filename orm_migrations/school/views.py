# from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.all().prefetch_related('teacher').order_by(ordering)
    context = {
        'object_list': students,
    }

    return render(request, template, context)
