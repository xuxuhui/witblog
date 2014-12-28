#coding:utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import Articles, SiteConf, Topics

# Create your views here.
def index(request):
	article = Articles.objects.all()
	
	return render(request, 'homepage.html', {'articles':article})

def aboutme(request):
	siteinfo = SiteConf.objects.get(pk=1)

	return render(request, 'aboutme.html', {'siteinfo':siteinfo})

def topic(request):
	topics = Topics.objects.all()

	return render(request, 'topic.html', {'topics':topics})

def like(request):

	return render(request, 'aboutme.html', {})

def reply(request):

	return render(request, 'aboutme.html', {})

def article(request, article_id):
	siteinfo = SiteConf.objects.get(pk=1)
	article = Articles.objects.get(id=article_id)
	
	return render(request, 'article.html', {'article':article, 'siteinfo':siteinfo})

def label(request, article_label):
	return render(request, 'articlelabel.html', {})

def topicsArticles(request, topic_id):
	article = Articles.objects.all().filter(topics_id=topic_id)
	
	return render(request, 'topicArticles.html', {"articles":article})

def likeit(reequest, article_id):
	likecount = 0
	article = Articles.objects.get(id=article_id)
	likecount = article.like + 1
	article.like = likecount

	article.save()

	return HttpResponse(likecount)
