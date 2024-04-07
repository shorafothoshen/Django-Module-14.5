from django.urls import path
from . import views
urlpatterns = [
    path("",views.Form,name="htmlForm"),
    path("Details/",views.Details,name="formDetails"),
]
