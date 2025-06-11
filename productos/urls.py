from django.urls import path
from . import views
from .views import ProductoAPIView


urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('api/', ProductoAPIView.as_view(), name='api_productos'),
    path('catalogo/', views.catalogo, name='catalogo'),

]
