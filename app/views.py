from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def contact(request):
    return render(request, 'app/contact.html')

def cart(request):
    return render(request, 'app/cart.html')

def news(request):
    return render(request, 'app/news.html')

def shop(request):
    return render(request, 'app/shop.html')

def books(request):
    return render(request, 'app/books.html')

def stationary(request):
    return render(request, 'app/stationary.html')

def single_product(request):
    return render(request, 'app/single-product.html')