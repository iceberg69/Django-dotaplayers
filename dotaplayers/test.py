
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
		print(self.pageinfo)
	def get_title(self):
		tpattern=r"<li.*?data-rid=\'%s\'>.+?<a href=.*?title=\"(.{1,15})\".*?>"%(self.roomid)
		li = re.findall(tpattern,self.pageinfo,re.S)
		if not li:
			return li
		else:
			return li.pop()
	def get_img(self):
		ipattern=r"<li.*?data-rid=\'%s\'.*?src=\'(.{1,50})\'.*?</img>"%(self.roomid)
		li = re.findall(ipattern,self.pageinfo,re.S)
		print(li)
		if not li:
			return li
		else:
			return li.pop()
		
	
if __name__=="__main__":
	live = douyu_spider(73966)
	print(live.get_title())
	print(live.get_img())
