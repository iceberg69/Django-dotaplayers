
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
		
	
if __name__=="__main__":
	
	roomlist=Live.objects.all()
	for roomid in roomlist:
		live = douyu_spider(roomid.slug)
		if not live.get_title():
			pass
		else:
			roomid.live_title=live.get_title()

		if not live.get_img():
			pass
		else:
			roomid.live_img=live.get_img()
		roomid.save()
	print('DONE')
