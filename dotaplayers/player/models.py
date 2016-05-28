from django.db import models
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse

class Player(models.Model):
	name=models.CharField('名称',max_length=20,default='')
	nick_name=models.CharField('ID',max_length=20,unique=True,default='')
	age=models.CharField('年龄',max_length=20,default='')
	nationality=models.CharField('国籍',max_length=10,default='')
	team=models.CharField('战队',max_length=10,default='')
	intro=UEditorField('简介',height=300,width=1000,default=u'',blank=True,imagePath="uploads/images/",toolbars='besttome',filePath='uploads/files/')
	home_display = models.BooleanField('首页显示',default=False)
	
#	intro=models.TextField('简介',default='')
	playerImage=models.ImageField(upload_to='photos')
	slug=models.CharField('网址',max_length=256,default='')

	def get_url(self):
		return reverse('player',args=(self.slug,))

	def __str__(self):
		return self.nick_name

	class Meta:
		verbose_name='选手'
		verbose_name_plural='选手'

class News(models.Model):
	title = models.CharField('标题',max_length=50)
	author = models.CharField('作者',max_length=25)
	content=UEditorField('内容',height=300,width=1000,default=u'',blank=True,imagePath="uploads/images/",toolbars='besttome',filePath='uploads/files/')
#	content=models.TextField('内容',default='')
	slug=models.CharField('网址',max_length=120,db_index=True)
	home_display = models.BooleanField('首页显示',default=False)

	def get_url(self):
		return reverse('news',args=(self.slug,))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='新闻'
		verbose_name_plural='新闻'

class Video(models.Model):
	video_name = models.CharField('视频名称',max_length=25,default='')
	author = models.CharField('作者',max_length=20)
	videoslug = models.CharField('视频网址',max_length=256,default='')
	slug = models.CharField('网址',max_length=120,default='')
	image = models.ImageField(upload_to='videocover',default='')
	home_display = models.BooleanField('首页显示',default=False)

	def get_url(self):
		return reverse('video',args=(self.slug,))


	def __str__(self):
		return self.video_name

	class Meta:
		verbose_name = '视频'
		verbose_name_plural = '视频'

class Live(models.Model):
	live_title = models.CharField('直播间名称',max_length=25,default='')
	live_slug = models.CharField('直播间网址',max_length=256,default='')
	live_img = models.CharField('直播间缩略图',max_length=256,default='')
	live_player = models.CharField('直播间所属选手',max_length=20,default='')
	slug = models.CharField('网址',max_length=120,default='')
	home_display = models.BooleanField('首页显示',default=False)
	def get_url(self):
		return reverse('live',args=(self.slug,))

	def __str__(self):
		return self.live_title

	class Meta:
		verbose_name = '直播'
		verbose_name_plural = '直播'



