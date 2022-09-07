from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('AppCoderInicio')),
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path('UserCoder/', include('UserCoder.urls')),
    ]
