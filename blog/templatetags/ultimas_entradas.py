from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('tags/ultimas_entradas.html')

def ultimas_entradas(n=5):
	return {
	'template':template,
	'ultimas_entradas':Post.objects.filter(estado='p')[:n]
	}