from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('webapp.urls')),   # including all of the urls from the webapp
    path('admin/', admin.site.urls),
]
