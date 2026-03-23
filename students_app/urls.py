from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home, name="home_page"),
    path("students_list", views.Students, name="students_list_page"),
    path("contact", views.ContactUs, name="contact_us_page"),
]
