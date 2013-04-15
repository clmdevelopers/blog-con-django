#encoding:utf-8
from django.contrib.syndication.views import Feed
from blog.models import Post
from django.utils.feedgenerator import Atom1Feed

#title, link y description corresponden al estandar RSS <title>, <link>, <description> respectivamente.
#item() es un simple metodo que retorna una lista de objetos que deben ser incluidos en el feed como <item> elementos.
#Cada item tiene un <title>, <link>, <description> nosotros debemos decirle al framework que datos poner en cada uno.
#Para especificar el contenido de <link>, hay dos opciones:
# - Por cada ítem en items(), Django primero tratará de ejecutar el método get_absolute_url() que previamente definimos en nuestro modelo. 
# Si dicho método no existe, entonces 
# - trata de llamar al método item_link() en la clase Feed, pasándole un único parámetro, item, que es el objeto en sí mismo.
#De igual forma pasamos los argumentos de los feeds para mostrar el otro tipo de sindicación atom

class RssEntradas(Feed):
	title 		= "Mi Blog"
	link 		= "/blog/"
	description = "Las últimas entradas de Mi Blog"

	def items(self):
		return Post.objects.all().order_by("-fecha")[:10]

	def item_title(self,item):
		return item.titulo

	def item_description(self, item):
		return item.contenido

class AtomSiteNewsFeed(RssEntradas):
	feed_type 	= Atom1Feed
	subtitle 	= RssEntradas.description
		
