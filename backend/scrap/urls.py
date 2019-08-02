from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListScrap.as_view()),
    path('<int:pk>/', views.DetailScrap.as_view()),
]