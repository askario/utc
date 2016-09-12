"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
	url(r'^about/$', 'landpage.views.about'),
	url(r'^news/all/$', 'landpage.views.all_news'),
	url(r'^page/(\d+)/$', 'landpage.views.all_news'),
	url(r'^news/get/(?P<news_id>\d+)/$', 'landpage.views.news'),
	url(r'^news/addlike/(?P<news_id>\d+)/$', 'landpage.views.addlike'),
    url(r'^news/addcomment/(?P<news_id>\d+)/$', 'landpage.views.addcomment'),
    url(r'^$', 'landpage.views.landpage'),
]
