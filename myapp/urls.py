from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('track_order/', views.track_order, name='track_order'),
]


htmxpatterns = [
    path('create_order/<int:pk>/', views.create_order, name='create_order')
]

urlpatterns += htmxpatterns