from django.urls import path
from . import views

app_name = "shouts"

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<int:id>/update/', views.update, name='update'),
]