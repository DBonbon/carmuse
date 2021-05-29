"""e_museum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from users import views as user_views

urlpatterns = [
    path('', include('homepage.urls',)),
    path('admin/', admin.site.urls, name=admin),
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('blogi/', include('blogi.urls')),
    path('contact/', include('contact.urls')),
    path('exhibitions/', include('exhibitions.urls')),
    path('users/', include('users.urls')),
    # path('register/', user_views.register, name='register'),
    # url(r"^", include("users.urls")),
    # path('dashboard/', include("users.urls")),
    # path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)