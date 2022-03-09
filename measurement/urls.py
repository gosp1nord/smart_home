from django.urls import path
from .views import temperature_create_view, SensorUpdateView, SensorRetrieveView, SensorListView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensor/', temperature_create_view),
    path('sensor/up/<pk>/', SensorUpdateView.as_view()),
    path('sensor/<pk>/', SensorRetrieveView.as_view()),
]
