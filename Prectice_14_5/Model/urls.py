from django.urls import path
from . import views
urlpatterns = [
    path("model_form/",views.modelForm,name="Model"),
]
