from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_pets/pages/home.html')

def about(request):
    return render(request, 'app_pets/pages/about.html')