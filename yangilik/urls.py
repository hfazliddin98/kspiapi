from django.urls import path
from .views import YangilikView, ElonView

urlpatterns = [
    path('yangilik/', YangilikView.as_view()),
    path('elon/', ElonView.as_view()),

]