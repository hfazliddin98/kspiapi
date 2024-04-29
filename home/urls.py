from django.urls import path
from .views import YangilikListAPIView, YangilikRetrieveAPIView, YangilikCreateAPIView, YangilikUpdateAPIView, YangilikDestroyAPIView
from .views import ElonListAPIView, ElonRetrieveAPIView, ElonCreateAPIView, ElonUpdateAPIView, ElonDestroyAPIView
from .views import GalareyaTuriListAPIView, GalareyaTuriRetrieveAPIView, GalareyaTuriCreateAPIView, GalareyaTuriUpdateAPIView, GalareyaTuriDestroyAPIView
from .views import GalareyaListAPIView, GalareyaRetrieveAPIView, GalareyaCreateAPIView, GalareyaUpdateAPIView, GalareyaDestroyAPIView
from .views import FikrListAPIView, FikrRetrieveAPIView, FikrCreateAPIView, FikrUpdateAPIView, FikrDestroyAPIView
from .views import TalabaListAPIView, TalabaRetrieveAPIView, TalabaCreateAPIView, TalabaUpdateAPIView, TalabaDestroyAPIView
from .views import HamkorlarimizListAPIView, HamkorlarimizRetrieveAPIView, HamkorlarimizCreateAPIView, HamkorlarimizUpdateAPIView, HamkorlarimizDestroyAPIView
from .views import StatistikaListAPIView, StatistikaRetrieveAPIView, StatistikaCreateAPIView, StatistikaUpdateAPIView, StatistikaDestroyAPIView
from .views import ElektronKutubxonaListAPIView, ElektronKutubxonaRetrieveAPIView, ElektronKutubxonaCreateAPIView, ElektronKutubxonaUpdateAPIView, ElektronKutubxonaDestroyAPIView
from .views import VideoMaruzalarListAPIView, VideoMaruzalarRetrieveAPIView, VideoMaruzalarCreateAPIView, VideoMaruzalarUpdateAPIView, VideoMaruzalarDestroyAPIView
from .views import VirtualQabulxonaListAPIView, VirtualQabulxonaRetrieveAPIView, VirtualQabulxonaCreateAPIView, VirtualQabulxonaUpdateAPIView, VirtualQabulxonaDestroyAPIView
from .views import MasofaviyTalimListAPIView, MasofaviyTalimRetrieveAPIView, MasofaviyTalimCreateAPIView, MasofaviyTalimUpdateAPIView, MasofaviyTalimDestroyAPIView
from .views import FakultetListAPIView, FakultetRetrieveAPIView, FakultetCreateAPIView, FakultetUpdateAPIView, FakultetDestroyAPIView



urlpatterns = [
    # yangilik
    path('yangilik/', YangilikListAPIView.as_view()),    
    path('yangilik/<int:pk>/', YangilikRetrieveAPIView.as_view()),
    path('yangilik/create/', YangilikCreateAPIView.as_view()),
    path('yangilik/update/<int:pk>/', YangilikUpdateAPIView.as_view()),
    path('yangilik/delete/<int:pk>/', YangilikDestroyAPIView.as_view()),

    # elon
    path('elon/', ElonListAPIView.as_view()),    
    path('elon/<int:pk>/', ElonRetrieveAPIView.as_view()),
    path('elon/create/', ElonCreateAPIView.as_view()),
    path('elon/update/<int:pk>/', ElonUpdateAPIView.as_view()),
    path('elon/delete/<int:pk>/', ElonDestroyAPIView.as_view()),

    #  galareya turi
    path('galareya/tur/', GalareyaTuriListAPIView.as_view()),    
    path('galareya/tur/<int:pk>/', GalareyaTuriRetrieveAPIView.as_view()),
    path('galareya/tur/create/', GalareyaTuriCreateAPIView.as_view()),
    path('galareya/tur/update/<int:pk>/', GalareyaTuriUpdateAPIView.as_view()),
    path('galareya/tur/delete/<int:pk>/', GalareyaTuriDestroyAPIView.as_view()),

    # galareya
    path('galareya/', GalareyaListAPIView.as_view()),    
    path('galareya/<int:pk>/', GalareyaRetrieveAPIView.as_view()),
    path('galareya/create/', GalareyaCreateAPIView.as_view()),
    path('galareya/update/<int:pk>/', GalareyaUpdateAPIView.as_view()),
    path('galareya/delete/<int:pk>/', GalareyaDestroyAPIView.as_view()),

    # fikr
    path('fikr/', FikrListAPIView.as_view()),    
    path('fikr/<int:pk>/', FikrRetrieveAPIView.as_view()),
    path('fikr/create/', FikrCreateAPIView.as_view()),
    path('fikr/update/<int:pk>/', FikrUpdateAPIView.as_view()),
    path('fikr/delete/<int:pk>/', FikrDestroyAPIView.as_view()),  
      
    # talaba
    path('talaba/', TalabaListAPIView.as_view()),    
    path('talaba/<int:pk>/', TalabaRetrieveAPIView.as_view()),
    path('talaba/create/', TalabaCreateAPIView.as_view()),
    path('talaba/update/<int:pk>/', TalabaUpdateAPIView.as_view()),
    path('talaba/delete/<int:pk>/', TalabaDestroyAPIView.as_view()),  

    # hamkorlarimiz
    path('hamkorlarimiz/', HamkorlarimizListAPIView.as_view()),    
    path('hamkorlarimiz/<int:pk>/', HamkorlarimizRetrieveAPIView.as_view()),
    path('hamkorlarimiz/create/', HamkorlarimizCreateAPIView.as_view()),
    path('hamkorlarimiz/update/<int:pk>/', HamkorlarimizUpdateAPIView.as_view()),
    path('hamkorlarimiz/delete/<int:pk>/', HamkorlarimizDestroyAPIView.as_view()),  

    # statistika
    path('statistika/', StatistikaListAPIView.as_view()),    
    path('statistika/<int:pk>/', StatistikaRetrieveAPIView.as_view()),
    path('statistika/create/', StatistikaCreateAPIView.as_view()),
    path('statistika/update/<int:pk>/', StatistikaUpdateAPIView.as_view()),
    path('statistika/delete/<int:pk>/', StatistikaDestroyAPIView.as_view()), 

    # ElektronKutubxona
    path('elektronkutubxona/', ElektronKutubxonaListAPIView.as_view()),    
    path('elektronkutubxona/<int:pk>/', ElektronKutubxonaRetrieveAPIView.as_view()),
    path('elektronkutubxona/create/', ElektronKutubxonaCreateAPIView.as_view()),
    path('elektronkutubxona/update/<int:pk>/', ElektronKutubxonaUpdateAPIView.as_view()),
    path('elektronkutubxona/delete/<int:pk>/', ElektronKutubxonaDestroyAPIView.as_view()), 

    # VideoMaruzalar
    path('videomaruzalar/', VideoMaruzalarListAPIView.as_view()),    
    path('videomaruzalar/<int:pk>/', VideoMaruzalarRetrieveAPIView.as_view()),
    path('videomaruzalar/create/', VideoMaruzalarCreateAPIView.as_view()),
    path('videomaruzalar/update/<int:pk>/', VideoMaruzalarUpdateAPIView.as_view()),
    path('videomaruzalar/delete/<int:pk>/', VideoMaruzalarDestroyAPIView.as_view()),  

    # VirtualQabulxona
    path('virtualqabulxona/', VirtualQabulxonaListAPIView.as_view()),    
    path('virtualqabulxona/<int:pk>/', VirtualQabulxonaRetrieveAPIView.as_view()),
    path('virtualqabulxona/create/', VirtualQabulxonaCreateAPIView.as_view()),
    path('virtualqabulxona/update/<int:pk>/', VirtualQabulxonaUpdateAPIView.as_view()),
    path('virtualqabulxona/delete/<int:pk>/', VirtualQabulxonaDestroyAPIView.as_view()),  

    # MasofaviyTalim
    path('masofaviytalim/', MasofaviyTalimListAPIView.as_view()),    
    path('masofaviytalim/<int:pk>/', MasofaviyTalimRetrieveAPIView.as_view()),
    path('masofaviytalim/create/', MasofaviyTalimCreateAPIView.as_view()),
    path('masofaviytalim/update/<int:pk>/', MasofaviyTalimUpdateAPIView.as_view()),
    path('masofaviytalim/delete/<int:pk>/', MasofaviyTalimDestroyAPIView.as_view()),  

    # Fakultet
    path('fakultet/', FakultetListAPIView.as_view()),    
    path('fakultet/<int:pk>/', FakultetRetrieveAPIView.as_view()),
    path('fakultet/create/', FakultetCreateAPIView.as_view()),
    path('fakultet/update/<int:pk>/', FakultetUpdateAPIView.as_view()),
    path('fakultet/delete/<int:pk>/', FakultetDestroyAPIView.as_view()),  

]