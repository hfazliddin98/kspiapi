from django.urls import path
from .views import YangilikView, ElonView, GalareyaTuriView, GalareyaView

urlpatterns = [
    path('yangilik/', YangilikView.as_view()),
    path('elon/', ElonView.as_view()),
    path('galareya/tur/', GalareyaTuriView.as_view()),
    path('galareya/', GalareyaView.as_view()),
]