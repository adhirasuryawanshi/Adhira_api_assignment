from rest_framework import generics
from .models import BogieChecksheet, WheelSpecification
from .serializer import BogieChecksheetSerializer, WheelSpecificationSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BogieChecksheetCreateAPIView(generics.CreateAPIView):
    queryset = BogieChecksheet.objects.all()
    serializer_class = BogieChecksheetSerializer

class WheelSpecificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bogie_number', 'inspection_date']

class BogieChecksheetListAPIView(generics.ListAPIView):
    queryset = BogieChecksheet.objects.all()
    serializer_class = BogieChecksheetSerializer