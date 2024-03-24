from django.urls import path
from .views import YangilikView, SinovView, MalumotView

urlpatterns = [
    path('', YangilikView.as_view()),
    path('sinov/', SinovView.as_view()),
    path('malumot/', MalumotView.as_view()),
]