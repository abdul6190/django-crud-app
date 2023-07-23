from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.

def home(request):
    all_students = Student.objects.all()
    return render(request, "student/index.html", context={'all_students':all_students})

def delete(request, id):
    Student.objects.get(id=id).delete()
    return redirect('home')

def add(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        phone = request.POST['phone']
        stu = Student(first_name=first_name, last_name=last_name, contact=phone)
        stu.save()
        return redirect('home')

    return render(request, "student/add.html")


def edit(request, id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':
        stu.first_name = request.POST['first-name']
        stu.last_name = request.POST['last-name']
        stu.contact = request.POST['phone']
        stu.save()
        return redirect('home')

    return render(request, 'student/edit.html', context={'student':stu})