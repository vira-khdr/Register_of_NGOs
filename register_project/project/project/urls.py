"""project URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
import register.views
admin.autodiscover()

urlpatterns = (
    url(r'^register_commerce_chamberce/add_commerce/$', 'register.views.add_commerse_chambers'),
    url(r'^register_commerce_chamberce/$', 'register.views.page_commerse_chambers'),

    url(r'^register_party/add_party/$', 'register.views.add_party'),
    url(r'^register_party/$', 'register.views.page_party'),

    url('', 'register.views.index'),
    url(r'^admin/', admin.site.urls),
)