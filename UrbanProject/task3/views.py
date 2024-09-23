from django.shortcuts import render

def main_page(request):
    return render(request, 'third_task/main_page.html')

def shop_page(request):
    items = {
        'Игра 1': '1000 руб',
        'Игра 2': '1500 руб',
        'Игра 3': '2000 руб'
    }
    return render(request, 'third_task/shop_page.html', {'items': items})

def cart_page(request):
    return render(request, 'third_task/cart_page.html')
