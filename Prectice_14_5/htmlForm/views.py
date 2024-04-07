from django.shortcuts import render

# Create your views here.
def Details(request):
    if request.method=="POST":
        name=request.POST.get("username")
        email=request.POST.get("useremail")
        rating=request.POST.get("select")
        return render(request,"Form/details.html",{"name":name,"email":email,"rating":rating})
    else:
        return render(request,"Form/details.html")


def Form(request):
    return render(request,"Form/htmlForm.html")