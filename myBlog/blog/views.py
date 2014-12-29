#coding:utf-8

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import Articles, SiteConf, Topics

# Create your views here.
def index(request):
	article_list = Articles.objects.order_by('-id')
	new = newPublish()
	articles = list(request, article_list)

	return render(request, 'homepage.html', {'articles':articles,'new':new})

def aboutme(request):
	siteinfo = SiteConf.objects.get(pk=1)
	new = newPublish()

	return render(request, 'aboutme.html', {'siteinfo':siteinfo, 'new':new})

def topic(request):
	topics = Topics.objects.all()
	new = newPublish()

	return render(request, 'topic.html', {'topics':topics, 'new':new})

def like(request):
	new = newPublish()
	article_list = Articles.objects.order_by("-like")
	articles = list(request, article_list)

	return render(request, 'homepage.html', {'articles':articles,'new':new})

def reply(request):

	return render(request, 'aboutme.html', {})

def article(request, article_id):
	new = newPublish()
	siteinfo = SiteConf.objects.get(pk=1)
	article = Articles.objects.get(id=article_id)
	
	return render(request, 'article.html', {'article':article, 'siteinfo':siteinfo, 'new':new})

def label(request, article_label):
	new = newPublish()
	article_list = Articles.objects.all().filter(label=article_label)
	articles = list(request, article_list)

	return render(request, 'homepage.html', {'articles':articles,'new':new})

def topics(request, topic_id):
	new = newPublish()
	article = Articles.objects.all().filter(topics_id=topic_id)
	return render(request, 'topicArticles.html', {'articles':article, 'new':new})

def topicsArticles(request, topic_id):
	new = newPublish()
	article_list = Articles.objects.all().filter(topics_id=topic_id)
	articles = list(request, article_list)
	
	return render(request, 'homepage.html', {"articles":articles, 'new':new})

def likeit(reequest, article_id):
	likecount = 0
	article = Articles.objects.get(id=article_id)
	likecount = article.like + 1
	article.like = likecount

	article.save()

	return HttpResponse(likecount)

def subjects(request, subjects_id):
	new = newPublish()
	article_list = Articles.objects.all().filter(topics_id=subjects_id)
	articles = list(request, article_list)

	return render(request, 'homepage.html', {'articles':articles,'new':new})

def newPublish():
	article = {}
	articleNew = Articles.objects.order_by('-id')[0:8]
	mjkf = Articles.objects.all().filter(topics_id=1).count()
	web= Articles.objects.all().filter(topics_id=2).count()
	shfx = Articles.objects.all().filter(topics_id=3).count()
	sfyj = Articles.objects.all().filter(topics_id=4).count()
	python = Articles.objects.all().filter(topics_id=5).count()
	django = Articles.objects.all().filter(topics_id=6).count()

	article['new'] = articleNew
	article['mjkf'] = mjkf
	article['web'] = web
	article['shfx'] = shfx
	article['sfyj'] = sfyj
	article['python'] = python
	article['django'] = django

	return article

def list(request, article):
	article_list = article
	paginator = Paginator(article_list, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	try:
		articles = paginator.page(page)
	except (EmptyPage, InvalidPage):
		articles = paginator.page(paginator.num_pages)

	return articles

def listing(request):
	pass
