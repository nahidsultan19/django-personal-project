from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


from . models import Employee
from .forms import EmployeeForm


# @login_required
def index(request):
    employee = Employee.objects.all()
    context = {'employees': employee}
    return render(request, 'emp.html', context)


def Detail(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(employee, many=True)
    context = {
        'employee': employee,
        'form': form
    }
    return render(request, context)
