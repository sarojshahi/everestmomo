from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def ourmenu(request):
    return render(request, 'ourmenu.html')

def ourservices(request):
    return render(request, 'ourservices.html')

def allergydevices(request):
    return render(request, 'allergydevices.html')