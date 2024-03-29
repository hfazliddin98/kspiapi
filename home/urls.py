from django.urls import path
from .views import YangilikListAPIView, YangilikCreateAPIView, YangilikUpdateAPIView, YangilikDestroyAPIView
from .views import ElonListAPIView, ElonCreateAPIView, ElonUpdateAPIView, ElonDestroyAPIView
from .views import GalareyaTuriListAPIView, GalareyaTuriCreateAPIView, GalareyaTuriUpdateAPIView, GalareyaTuriDestroyAPIView
from .views import GalareyaListAPIView, GalareyaCreateAPIView, GalareyaUpdateAPIView, GalareyaDestroyAPIView

urlpatterns = [
    path('yangilik/get/', YangilikListAPIView.as_view()),
    path('yangilik/post/', YangilikCreateAPIView.as_view()),
    path('yangilik/update/', YangilikUpdateAPIView.as_view()),
    path('yangilik/delete/', YangilikDestroyAPIView.as_view()),

    # elon uchun
    path('elon/get/', ElonListAPIView.as_view()),
    path('elon/post/', ElonCreateAPIView.as_view()),
    path('elon/update/', ElonUpdateAPIView.as_view()),
    path('elon/delete/', ElonDestroyAPIView.as_view()),

    #  galareya turi
    path('galareya/tur/get/', GalareyaTuriListAPIView.as_view()),
    path('galareya/tur/post/', GalareyaTuriCreateAPIView.as_view()),
    path('galareya/tur/update/', GalareyaTuriUpdateAPIView.as_view()),
    path('galareya/tur/delete/', GalareyaTuriDestroyAPIView.as_view()),

    # galareya
    path('galareya/get/', GalareyaListAPIView.as_view()),
    path('galareya/post/', GalareyaCreateAPIView.as_view()),
    path('galareya/update/', GalareyaUpdateAPIView.as_view()),
    path('galareya/delete/', GalareyaDestroyAPIView.as_view()),
]