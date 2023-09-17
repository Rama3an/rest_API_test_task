from .views import CurrentAPIView
from django.urls import path

urlpatterns = [
    path('api/rates', CurrentAPIView.as_view()),
]
