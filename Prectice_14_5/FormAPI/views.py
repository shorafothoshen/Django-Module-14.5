from django.shortcuts import render
from .forms import precticeForm
# Create your views here.

def FormAPI(request):
    if request.method=="POST":
        pF=precticeForm(request.POST)
        if pF.is_valid():
            print(pF.cleaned_data)
    else:
        pF=precticeForm()
    return render(request,"Api/formapi.html",{"pF":pF})






