from django import template
from blog.models import Categoria

register = template.Library()

@register.inclusion_tag('tags/ultimas_categorias.html')

def ultimas_categorias(n=5):
	#Retorna n categorias
	return {
	'template':template,
	'ultimas_categorias': Categoria.objects.filter()[:n]
	}