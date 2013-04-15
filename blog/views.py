# Create your views here.
from blog.models import Post, Categoria
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView

def tagpage(request, tag):
	post = Post.objects.filter(tags__name=tag)
	return render_to_response("tagpage.html",{
		"posts":post,
		"tag":tag
	})

def buscar(request):
	query = request.GET.get('q','')
	if query:
		qset = (
			Q(titulo__icontains=query)|
			Q(texto__icontains=query)
		)
		results = Post.objects.filter(qset)
	else:
		results = []
	return render_to_response('search.html',{
		'results': results,
		'query': query
	})

class ListaCategorias(ListView):
	#Retorna todas las entradas por Categoria
	template_name = '/blog/templates/categorias.html'
	paginate_by = 10

	def get_queryset(self):
		print "hola xD"
		categoria = get_object_or_404(Categoria, slug__exact=self.kwargs['slug'])
		return Post.objects.filter(categoria=categoria)

	def get_context_data(self, **kwargs):
		context 				= super(ListaCategorias, self).get_context_data(**kwargs)
		context['entradas'] 	= Post.objects.filter(categoria =self.categoria)
		context['categorias'] 	= Categoria.objects.get(nombre =self.categoria)
		return context