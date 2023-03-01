from django.urls import path
from . import views

urlpatterns=[
    path('', views.all_doctors, name='doctors'),
    path('doctors/<int:departmnetId>', views.doctors, name='doctors_by_departments'),
    path('doctors-details/<int:doctorId>', views.doctor_details, name='doctor-details')
]