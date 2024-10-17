from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("name/", myname, name="myname"),
    path("groupe/", groupe, name="groupe"),
    path("age/", age, name="age"),
    path("common/", common, name="common"),
    path("", common, name="common"),
]

