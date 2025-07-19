from django.urls import path
from .views import *

urlpatterns = [
    path('forms/bogie-checksheet', BogieChecksheetCreateAPIView.as_view()),
    path('forms/bogie-checksheet-list', BogieChecksheetListAPIView.as_view()),
    path('forms/wheel-specifications', WheelSpecificationListCreateAPIView.as_view()),
]
