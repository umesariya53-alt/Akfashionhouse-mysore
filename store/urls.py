from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:cat_name>/', views.category_view, name='category'),
]
