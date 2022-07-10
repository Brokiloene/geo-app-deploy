from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('search/', include('core.urls')),
    path('admin/', admin.site.urls),
]
