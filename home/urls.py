from django.urls import path
from .views import YangilikListAPIView, YangilikCreateAPIView, ElonView, GalareyaTuriView, GalareyaView

urlpatterns = [
    path('yangilik/get/', YangilikListAPIView.as_view()),
    path('yangilik/post/', YangilikCreateAPIView.as_view()),
    path('elon/', ElonView.as_view()),
    path('galareya/tur/', GalareyaTuriView.as_view()),
    path('galareya/', GalareyaView.as_view()),
]