from django.shortcuts import render
from django.http import HttpResponse
from player.models import Player,News,Video,Live

def index(request):
	playerlist = Player.objects.filter(home_display=True)
	newslist = News.objects.filter(home_display=True)
	videolist = Video.objects.filter(home_display=True)
	livelist = Live.objects.filter(home_display=True)
	return render(request,'index.html',{'playerlist':playerlist,'newslist':newslist,'videolist':videolist,'livelist':livelist})

def mainplayer(request):
	playerlist = Player.objects.all()
	return render(request,'mainplayer.html',{'playerlist':playerlist})

def mainnews(request):
	newslist = News.objects.all()
	return render(request,'mainnews.html',{'newslist':newslist})

def mainvideo(request):
	videolist = Video.objects.all()
	return render(request,'mainvideo.html',{'videolist':videolist})

def mainlive(request):
	livelist = Live.objects.all()
	return render(request,'mainlive.html',{'livelist':livelist})

def player_detail(request,player_slug):
	player = Player.objects.get(slug=player_slug)
	return render(request,'player.html',{'player':player})

def news_detail(request,news_slug):
	news = News.objects.get(slug=news_slug)
	return render(request,'news.html',{'news':news})

def video_detail(request,video_slug):
	video = Video.objects.get(slug=video_slug)
	return render(request,'video.html',{'video':video})

def live_detail(request,live_slug):
	live = Live.objects.get(slug=live_slug)
	return render(request,'live.html',{'live':live})
