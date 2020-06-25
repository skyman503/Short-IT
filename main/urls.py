from django.urls import path
from .views import index, add_url, connect

# 'main' url handling

urlpatterns = [
    path('', index, name='index'),
    path('add_url/', add_url, name='add_url'),
    path('r/<str:new_url>', connect, name='connect')
]
