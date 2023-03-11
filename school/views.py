from django.views.generic import ListView
from django.shortcuts import render

from .models import Student

def students_list(request):
    template = 'school/students_list.html'
    #student = request.GET.get('students')
    object_list = Student.objects.all().prefetch_related('teachers')
    for student in object_list:
        print(student.teachers.all())
    context = {'object_list': object_list}
    ordering = 'group'

    return render(request, template, context)
