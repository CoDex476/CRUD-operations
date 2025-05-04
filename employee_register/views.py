from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee


def employee_form(request, id):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {"form": form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/employee/list")


def employee_list(request):
    employee_list = Employee.objects.all()
    context = {"employee_list": employee_list}
    return render(request, "employee_register/employee_list.html", context)


def employee_delete(request):
    return HttpResponse("<h1>delete page</h1>")
