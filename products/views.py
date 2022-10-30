from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Katalog'
    }
    return render(request, 'products/products.html', context) 


def test_context(request):
    context = {
        'title': 'store',
        'header': 'Dobro pojalovat',
        'username': 'Ivan Ivanov',
        'products': [
            {'name': 'xudi adidas', 'price': '1000'},
            {'name': 'c thenorthface', 'price': '15'},
            {'name': 'over design', 'price': '1800'}
        ],
        #'promotion': True,
        'products_of_promotion': [
            {'name': 'ryukzak cherniy', 'price':'25'},
        ]
    }
    return render(request, 'products/test-context.html', context)