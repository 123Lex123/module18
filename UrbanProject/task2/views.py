from django.shortcuts import render

# Функциональное представление
def function_view(request):
    return render(request, 'second_task/function_template.html')

# Классовое представление
from django.views import View

class ClassView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')
