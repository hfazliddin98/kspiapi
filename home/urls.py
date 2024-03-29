from django.urls import path
from .views import YangilikListAPIView, YangilikCreateAPIView, YangilikRetrieveUpdateDestroyAPIView
from .views import ElonListAPIView, ElonCreateAPIView, ElonRetrieveUpdateDestroyAPIView
from .views import GalareyaTuriListAPIView, GalareyaTuriCreateAPIView, GalareyaTuriRetrieveUpdateDestroyAPIView
from .views import GalareyaListAPIView, GalareyaCreateAPIView, GalareyaRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('yangilik/', YangilikListAPIView.as_view()),
    path('yangilik/post/', YangilikCreateAPIView.as_view()),
    path('yangilik/<int:pk>/', YangilikRetrieveUpdateDestroyAPIView.as_view()),

    # elon uchun
    path('elon/', ElonListAPIView.as_view()),
    path('elon/post/', ElonCreateAPIView.as_view()),
    path('elon/<int:pk>/', ElonRetrieveUpdateDestroyAPIView.as_view()),
    

    #  galareya turi
    path('galareya/tur/', GalareyaTuriListAPIView.as_view()),
    path('galareya/tur/post/', GalareyaTuriCreateAPIView.as_view()),
    path('galareya/tur/<int:pk>/', GalareyaTuriRetrieveUpdateDestroyAPIView.as_view()),

    # galareya
    path('galareya/', GalareyaListAPIView.as_view()),
    path('galareya/post/', GalareyaCreateAPIView.as_view()),
    path('galareya/<int:pk>/', GalareyaRetrieveUpdateDestroyAPIView.as_view()),
]