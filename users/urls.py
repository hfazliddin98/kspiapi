from django.urls import path
from .views import YangilikSearchView, ElonSearchView

urlpatterns = [
    path('yangilik_search/', YangilikSearchView.as_view(), name='yangilik_search'),
    path('elon_search/', ElonSearchView.as_view(), name='elon_search'),
]