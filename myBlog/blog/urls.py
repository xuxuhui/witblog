from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blog.views.index', name='index'),
	url(r'^about/$', 'blog.views.aboutme', name='aboutme'),
	url(r'^topic/$', 'blog.views.topic', name='topic'),
	url(r'^topicsArticles/(?P<topic_id>\d+)/$', 'blog.views.topicsArticles', name='topicsArticles'),
	url(r'^like/$', 'blog.views.like', name='like'),
	url(r'^likeit/(?P<article_id>\d+)/$', 'blog.views.likeit', name="likeit"),
	url(r'^reply/$', 'blog.views.reply', name='reply'),
	url(r'^article/(?P<article_id>\d+)/$', 'blog.views.article', name='article'),
	url(r'^articlelabel/(?P<article_label>\w+)/$', 'blog.views.label', name='label'),
	url(r'^topics/(?P<topic_id>\d+)/$', 'blog.views.topics', name='topiclabel'),

	url(r'^subjects/(?P<subjects_id>\d+)/$', 'blog.views.subjects', name='subjects'),
	url(r'^page/', 'blog.views.listing'),
)
