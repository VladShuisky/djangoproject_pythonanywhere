from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetCapitalInfoView.as_view()),
]