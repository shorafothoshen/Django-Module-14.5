from django.urls import path
from . import views
urlpatterns = [
    path("form_api/",views.FormAPI,name="APIForm"),
]
