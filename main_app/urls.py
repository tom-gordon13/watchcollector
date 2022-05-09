from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('watches/', views.watch_index, name='index'),
    path('watches/<int:watch_id>', views.watch_detail, name='detail'),
    path('watches/create/', views.WatchCreate.as_view(), name='watch_create'),
]