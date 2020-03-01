from django.urls import path

from prediction import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('result/', views.ResultView.as_view(), name='result'),
]