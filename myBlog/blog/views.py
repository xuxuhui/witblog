#coding:utf-8

from django.shortcuts import render, render_to_response
from blog.models import Topics, Articles, Comments,SiteConf
from django.http import HttpResponse

# Create your views here.
def index(request):
	articles = Articles.objects.all().order_by('-id')
	
	return render(request, 'index.html', {'articles':articles})

def topics(request):
	topics = Topics.objects.all()
	
	return render(request, 'topic.html', {'topics':topics})

def likest(request):
	return render(request, 'like.html', {})

def publish(request):
	return render(request, 'publish.html',{})

def publishSubmit(request):
	error = []
	if not ('head_line' in request.GET and request.GET['head_line']):
		head_line = '标题名字不能为空'
		error.append({'head_line':head_line})
	else:
		head = request.GET['head_line']

	if not ('article' in request.GET and request.GET['article']):
		cont= '内容不能为空'
		error.append({'content':cont})
	else:
		article = request.GET['article']

	if not error:
		Articles.objects.create(headline=head, content=article, image="uploadImages/web.jpeg", label="python", topics=Topics.objects.all()[1])

		return render_to_response('publish_success.html',{})
		

	return render(request, 'publish.html',{'error':error})

def topicsArticles(req, article_id):
	topics = Topics.objects.all()

	return render_to_response("topicArticles.html",{})

def articles(req, article_id):
	article = Articles.objects.get(pk = article_id)
	siteinfo = SiteConf.objects.get(pk=1)

	return render_to_response("article.html", {'article':article,"siteinfo":siteinfo})

def comments(req, article_id):
	pass

def likeit(request, article_id):
	likecount = 0;
	article = Articles.objects.get(id = article_id)
	likecount = article.like + 1
	article.like=likecount
	article.save()

	return HttpResponse(likecount)
