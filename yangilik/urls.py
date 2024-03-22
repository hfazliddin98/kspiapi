from django.urls import path
from .views import YangilikView

urlpatterns = [
    path('', YangilikView.as_view()),
]