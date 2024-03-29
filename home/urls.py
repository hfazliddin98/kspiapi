from django.urls import path
from .views import YangilikListAPIView, YangilikCreateAPIView, YangilikUpdateAPIView, YangilikDestroyAPIView
from .views import ElonView, GalareyaTuriView, GalareyaView

urlpatterns = [
    path('yangilik/get/', YangilikListAPIView.as_view()),
    path('yangilik/post/', YangilikCreateAPIView.as_view()),
    path('yangilik/update/', YangilikUpdateAPIView.as_view()),
    path('yangilik/delete/', YangilikDestroyAPIView.as_view()),

    # elon uchun
    path('elon/', ElonView.as_view()),
    path('galareya/tur/', GalareyaTuriView.as_view()),
    path('galareya/', GalareyaView.as_view()),
]