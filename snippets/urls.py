from django.urls import path
from . import views

urlpatterns = [
    path('snippet_list/', views.snippet_list),
    path('snippet_detail/<int:pk>/', views.snippet_detail)

]