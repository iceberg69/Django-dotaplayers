import re
import urllib.request

url = '张宁'
url = urllib.parse.quote(url)
url = 'http://baike.baidu.com/item/'+ url

allpage = urllib.request.urlopen(url).read().decode('UTF-8')

#rPattern=r'<dt .*?>游戏ID</dt>.<dd .*?>\n(.{1,10})\n</dd>'
rPattern=r'<sup>.*?</sup>'
id=re.findall(rPattern,allpage,re.S)
print(id)
#print(allpage)

'''
tex = '2.html'
f = open(tex,'w+')
f.write(allpage)
f.close()
'''


