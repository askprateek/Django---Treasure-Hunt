"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from .views import *

urlpatterns = [
    url(r'^$', custom_login, name='main_index.html'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='registration/register.html'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'registration/logout.html'}),
    url(r'^hunt/', include('hunt.urls')),
    url(r'^success/$', register_success)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
