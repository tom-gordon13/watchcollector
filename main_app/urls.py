from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('watches/', views.watch_index, name='index'),
    path('watches/<int:watch_id>', views.watch_detail, name='detail'),
    path('watches/create/', views.WatchCreate.as_view(), name='watch_create'),
    path('watches/<int:pk>/update/', views.WatchUpdate.as_view(), name='watch_update'),
    path('watches/<int:pk>/delete/', views.WatchDelete.as_view(), name='watch_delete'),
    path('watches/<int:watch_id>/add_servicing/', views.add_servicing, name='add_servicing'),
    path('watches/<int:watch_id>/assoc_comp/<int:component_id>/', views.assoc_comp, name='assoc_comp'),
    path('components/', views.ComponentList.as_view(), name='components_index'),
    path('components/<int:pk>/', views.ComponentDetail.as_view(), name='component_detail'),
    path('components/create/', views.ComponentCreate.as_view(), name='component_create'),
    path('components/<int:pk>/update/', views.ComponentUpdate.as_view(), name='component_update'),
    path('components/<int:pk>/delete/', views.ComponentDelete.as_view(), name='component_delete'),
]



