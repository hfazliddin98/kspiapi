from django.urls import path
from .views import InstitutHaqidaListAPIView, InstitutHaqidaRetrieveAPIView, InstitutHaqidaCreateAPIView, InstitutHaqidaUpdateAPIView, InstitutHaqidaDestroyAPIView


urlpatterns = [
    # inistiut haqida
    path('instituthaqida/', InstitutHaqidaListAPIView.as_view()),    
    path('instituthaqida/<int:pk>/', InstitutHaqidaRetrieveAPIView.as_view()),
    path('instituthaqida/create/', InstitutHaqidaCreateAPIView.as_view()),
    path('instituthaqida/update/<int:pk>/', InstitutHaqidaUpdateAPIView.as_view()),
    path('instituthaqida/delete/<int:pk>/', InstitutHaqidaDestroyAPIView.as_view()),

]