from django.shortcuts import render
from .models import Docotrs
from django.http import HttpResponse

# Create your views here.
def all_doctors(request):
    doctors = Docotrs.objects.all()
    return render(request, "doctors.html", {'doctors': doctors})


def doctors(request, departmnetId):
    doctors = Docotrs.objects.filter(department=departmnetId)
    return render(request, "doctors.html", {'doctors': doctors})


def doctor_details(request, doctorId):
    doctor = Docotrs.objects.filter(department=doctorId)
    return render(request, "date.html", {'doctors': doctor})




