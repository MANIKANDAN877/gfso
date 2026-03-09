from django.shortcuts import render
from .models import *

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        rollno = request.POST.get('rollno')

        Sret.objects.create(
            name=name,
            dept=dept,
            rollno=rollno
        )

    return render(request, 'mani.html')