#encoding:utf8

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
#创建topic表
class Topics(models.Model):
	#中文为数据库旁注，没有时会直接实现字段名:
	name = models.CharField('专题名称', max_length=40)
	discription = models.CharField('描述',max_length=200)
	image = models.ImageField('展示图片', upload_to='uploadImages')
	discretion_image = models.ImageField('专题图表', upload_to='uploadImages')

	#返回一个字段为数据库检索
	def __unicode__(self):
		return self.name

	#Meta的运用
	#verbose_name 数据库旁注名称
	#ordering 默认排序
	class Meta:
		verbose_name_plural = "专题"

	#创建文章数据库
class Articles(models.Model):
		headline = models.CharField('标题', max_length=100)
		content = models.CharField('内容', max_length=5000)
		pub_date = models.DateField('发布时间', default=timezone.now)
		image = models.ImageField('图片', upload_to="uploadImages")
		label = models.CharField('标签',default='默认标签',max_length=200)
		like = models.IntegerField('喜欢', default=0)
		topics = models.ForeignKey(Topics, verbose_name='所属专题')
		discuss = models.IntegerField('评论条数', default=0)
	
		def __unicode__(self):
			return self.headline

		class Meta:	
			verbose_name_plural = '文章'
#创建评论表
class Comments(models.Model):
	nickname = models.CharField('用户昵称', max_length=40)
	comment = models.CharField('评论内容', max_length=2000)
	artile	=models.ForeignKey(Articles, verbose_name='被评文章')
	pub_date = models.DateField('发布日期', default=datetime.datetime.today())

	def __unicode__(self):
		return self.nickname

	class Meta:
		verbose_name_plural = '评论'

#站点设置:
class SiteConf(models.Model):
	username = models.CharField('用户名称', max_length=40)
	user_signature = models.CharField('个性签名', max_length=200)
	index_image = models.ImageField('首页展示图片', upload_to='uploadImages')
	user_image = models.ImageField('用户头像', upload_to='uploadImages')

	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name_plural = '站点设置'
