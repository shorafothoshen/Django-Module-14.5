
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("FormAPI.urls")),
    path("",include("htmlForm.urls")),
    path("",include("Model.urls")),
]
