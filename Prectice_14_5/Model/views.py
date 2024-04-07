from django.shortcuts import render

# Create your views here.
def modelForm(request):
    return render(request,"model/showModel.html")