"""dotaplayers URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings

urlpatterns = [
	url(r'^$','player.views.index',name='index'),
	url(r'^player/$','player.views.mainplayer',name='mainplayer'),
	url(r'^news/$','player.views.mainnews',name='naminnews'),
	url(r'^video/$','player.views.mainvideo',name='mainvideo'),
	url(r'^live/$','player.views.mainlive',name='mainlive'),
	url(r'^ueditor/',include(DjangoUeditor_urls)),
    url(r'^admin/', admin.site.urls),
	url(r'^player/(?P<player_slug>[^/]+)/$','player.views.player_detail',name='player'),
	url(r'^news/(?P<news_slug>[^/]+)/$','player.views.news_detail',name='news'),
	url(r'^video/(?P<video_slug>[^/]+)/$','player.views.video_detail',name='video'),
	url(r'^live/(?P<live_slug>[^/]+)/$','player.views.live_detail',name='live'),

]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(
		settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
