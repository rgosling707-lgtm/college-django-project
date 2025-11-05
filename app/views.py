from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'main/home.html')

def indexView(request):
    return render(request, 'main/index.html')

def productsView(request):
    return render(request, 'main/products.html')