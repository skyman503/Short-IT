from django.contrib import admin
from django.urls import path, include

# main url handling

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
