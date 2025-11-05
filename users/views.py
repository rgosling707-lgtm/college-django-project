from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'main/login.html')

def register_view(request):
    return render(request, 'main/register.html')

def profile_view(request):
    return render(request, 'main/profile.html')