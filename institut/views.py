from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .models import InstitutHaqida
from .serialazer import InstitutHaqidaSerializer


class InstitutHaqidaListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = InstitutHaqida
    serializer_class = InstitutHaqidaSerializer
    queryset = InstitutHaqida.objects.all()

class InstitutHaqidaRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = InstitutHaqida
    serializer_class = InstitutHaqidaSerializer
    queryset = InstitutHaqida.objects.all()

class InstitutHaqidaCreateAPIView(CreateAPIView):
    metadata_class = InstitutHaqida
    serializer_class = InstitutHaqidaSerializer
    queryset = InstitutHaqida.objects.all()

class InstitutHaqidaUpdateAPIView(UpdateAPIView):
    metadata_class = InstitutHaqida
    serializer_class = InstitutHaqidaSerializer
    queryset = InstitutHaqida.objects.all()

class InstitutHaqidaDestroyAPIView(DestroyAPIView):
    metadata_class = InstitutHaqida
    serializer_class = InstitutHaqidaSerializer
    queryset = InstitutHaqida.objects.all()
