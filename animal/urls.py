from django.urls import path
from .views import AnimalView, AnimalById

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalById.as_view()),
]