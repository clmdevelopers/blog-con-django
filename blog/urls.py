from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.feeds import RssEntradas, AtomSiteNewsFeed
from blog.views import ListaCategorias

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
        model               = Post,
        context_object_name = 'entradas',
        template_name       = 'blog.html',
        paginate_by = 10,
    )),
    url(r'^feed/$', RssEntradas()),
    url(r'^atom/$', AtomSiteNewsFeed()),
    url(r'^buscar/$','buscar'),
    url(r'^archivos/$', ListView.as_view(
        queryset        = Post.objects.all().order_by("-fecha"),
    	template_name   = "archivos.html",
    	)),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^categoria/(?P<slug>[^\.]+)/', ListaCategorias.as_view(), name = 'categorias'),
    url(r'^(?P<slug>[^\.]+)/', DetailView.as_view(
        model               = Post,
        context_object_name = 'entradas',
        template_name       = 'post.html',
    ), name = 'entradas'),
)