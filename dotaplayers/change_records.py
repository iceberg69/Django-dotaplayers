'''
a spider for  player_player table
'''

from dotaplayers.wsgi import *
import urllib
import urllib.request
import re
from player.models import Player

class player_spider:	
	def __init__(self,url):
		self.url = url
		url = urllib.parse.quote(url)
		self.baikeurl = 'http://baike.baidu.com/item/'+url
		self.baikeinfo = urllib.request.urlopen(self.baikeurl).read().decode('UTF-8')

	def get_name(self):
		rPattern = r'<dt class="basicInfo-item name">中文名</dt>.<dd class="basicInfo-item value">\n(.{1,10})\n</dd>'
		pName=re.findall(rPattern,self.baikeinfo,re.S)
		try:
			return pName.pop()
		except Exception as err:
			return self.url

	
	def get_nickname(self):
		rPattern = r'<dt class="basicInfo-item name">外文名</dt>.<dd class="basicInfo-item value">\n(.{1,10})\n</dd>'
		id=re.findall(rPattern,self.baikeinfo,re.S)
		if not id:
			rPattern=r'<dt .*?>游戏ID</dt>.<dd .*?>\n(.{1,10})\n</dd>'
			id=re.findall(rPattern,self.baikeinfo,re.S)
		try:
			return id.pop()
		except Exception as err:
			return self.url
	
	def get_age(self):
		rPattern = r'<dt class="basicInfo-item name">出生日期</dt>.<dd class="basicInfo-item value">\n(.{1,5})年.{1,10}\n</dd>'
		age = re.findall(rPattern,self.baikeinfo,re.S)
		try:
			return (str)(2016-(int)(age.pop()))
		except Exception as err:
			return ''

	def get_nation(self):
		rPattern = r'<dt class="basicInfo-item name">国&nbsp;&nbsp;&nbsp;&nbsp;籍</dt>.<dd class="basicInfo-item value">\n(.{1,10})\n</dd>'
		nation = re.findall(rPattern,self.baikeinfo,re.S)
		try:
			return nation.pop()
		except Exception as err:
			return ''

	def get_intro(self):
		rPattern = r'</dl><div class="lemma-summary" label-module="lemmaSummary">.<div class="para" label-module="para">(.+?)</div>.</div>'
		intro = re.findall(rPattern,self.baikeinfo,re.S).pop()
		BgnCharToNoneRex = re.compile(r'(<p>|</p>|<a.*?>|</a>)')
		nbspToSpace = re.compile(r"(&nbsp|&quot);")
		supToNone = re.compile(r"<sup>.*?</sup>")
		intro = BgnCharToNoneRex.sub("",intro)
		intro = nbspToSpace.sub(" ",intro)
		intro = supToNone.sub("",intro)

		try:
			return intro
		except Exception as err:
			return ''

	def get_slug(self):
		return self.url


'''
url = input("请输入选手名称: ")
player = player_spider(url)
s = player.get_name()
i = player.get_id()
a = player.get_age()
n = player.get_nation()
intro = player.get_intro()
slug = player.get_slug()
print(s)
print(i)
print(a)
print(n)
print(intro)
print(slug)
'''

if __name__ == '__main__':
	list = ('徐志雷','卜严骏','陈智豪','张宁','雷增荣','mushi','骆非池','Dendi','龚建','伍声','820','黄福全')
#	for i in range(len(list)):
	player = player_spider("Dendi")
	changeplayer = Player.objects.get(name="Dendi")
	changeplayer.intro = player.get_intro()
	changeplayer.save()
		
	'''
	print(player.get_name())
	print(player.get_id())
	print(player.get_age())
	print(player.get_nation())
	print(player.get_intro())
	print(player.get_slug())
	'''
	print('Done')

