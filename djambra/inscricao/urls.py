from django.urls import path
from . import views
urlpatterns = [
    path('inscrito/', views.InscritoList.as_view(), name='inscrito-list'),
    path('inscrito/<int:pk>/', views.InscritoDetail.as_view(), name='inscrito-detail'),
]