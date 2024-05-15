from rest_framework.viewsets import ModelViewSet
from .models import InstitutHaqida
from .serialazer import InstitutHaqidaSerializer




class InstitutHaqidaViewSet(ModelViewSet):
    queryset = InstitutHaqida.objects.all()
    serializer_class = InstitutHaqidaSerializer
