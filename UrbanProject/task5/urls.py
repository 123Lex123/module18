from django.urls import path
from .views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('sign-up-django/', sign_up_by_django, name='sign_up_by_django'),
    path('sign-up-html/', sign_up_by_html, name='sign_up_by_html'),
]
