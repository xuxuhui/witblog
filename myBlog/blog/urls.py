from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blog.views.index', name='index'),
	url(r'^topics/$', 'blog.views.topics', name='topics'),
	url(r'^likest/', 'blog.views.likest', name='likest'),
	url(r'^publish/', 'blog.views.publish', name='publish'),
	url(r'^publishSubmit/', 'blog.views.publishSubmit', name='publishSubmit'),
	url(r'^likeit/(?P<article_id>\d+)/$', 'blog.views.likeit', name="likeit"),
	url(r'^topics/(?P<id>\d+)/$', 'blog.views.topicsArticles', name="topicsArticles"),
	url(r'^comments/(?P<article_id>\d+)/$', 'blog.views.comments', name="comments"),
	url(r'(?P<article_id>\d+)/$', 'blog.views.articles', name='articles'),
)
