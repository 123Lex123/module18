from django.shortcuts import render

def main_page(request):
    return render(request, 'fourth_task/main_page.html')

def shop_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    return render(request, 'fourth_task/shop_page.html', {'games': games})

def cart_page(request):
    return render(request, 'fourth_task/cart_page.html')
