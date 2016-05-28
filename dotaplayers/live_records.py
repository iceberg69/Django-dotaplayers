
from dotaplayers.wsgi import *
import urllib
import urllib.request
import re
from player.models import Live

class douyu_spider:
	def __init__(self,roomid):
		self.roomid=roomid
		self.url="http://www.douyu.com/directory/game/DOTA2"
		self.pageinfo = urllib.request.urlopen(self.url).read().decode('utf8')
	def get_title(self):
		tpattern=r"<li.*?data-rid=\'%s\'>.+?<a href=.*?title=\"(.{1,30})\".*?>"%(self.roomid)
		li = re.findall(tpattern,self.pageinfo,re.S)
		if not li:
			return li
		else:
			return li.pop()
	def get_img(self):
		ipattern=r"<li.*?data-rid=\'%s\'>.*?<img data-original=\"(.{1,60})\""%(self.roomid)
		li = re.findall(ipattern,self.pageinfo,re.S)
		if not li:
			return li
		else:
			return li.pop()
	def get_player(self):
		ppattern=r"<li.*?data-rid=\'%s\'>.*?<span class=\"dy-name ellipsis fl\">(.{1,20})</span>"%(self.roomid)
		li = re.findall(ppattern,self.pageinfo,re.S)
		if not li:
			return li
		else:
			return li.pop()
		
	
if __name__=="__main__":
	roomid = 0
	while 1:
		roomid = input("请输入房间号:\n")
		if roomid == 'q':
			break
		live = douyu_spider(roomid)
		roomlist=[]
		for room in Live.objects.all():
			roomlist.append(room.slug)
		if roomid in roomlist:
			print("直播间以存在!")
		else:
			if not live.get_player() and not live.get_title() and not live.get_img():
				pass
			else:
				room = Live.objects.get_or_create(
					live_title=live.get_title(),
					live_img=live.get_img(),
					live_player=live.get_player(),
					live_slug=roomid,
					slug=roomid,
				)
	print('DONE')
