from django.shortcuts import render
from .models import Student


def Home(request):
    return render(request, "home.html")


def Students(request):
    all_students = Student.objects.all()
    return render(request, "students.html", {"students": all_students})


def ContactUs(request):
    return render(request, "contact.html")
