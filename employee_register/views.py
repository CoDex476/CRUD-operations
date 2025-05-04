from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm


def employee_form(request):
    form = EmployeeForm()
    context = {"form": form}
    return render(request, "employee_register/employee_form.html", context)


def employee_list(request):
    return render(request, "employee_register/employee_list.html")


def employee_delete(request):
    return HttpResponse("<h1>delete page</h1>")
