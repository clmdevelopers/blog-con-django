#encoding:utf-8
from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.db.models import permalink

#tipos de entradas: publicada y borrador
ESTADO = (
	('b','Borrador'),
	('p','Publicado'),
)

#Clase para las Categorias de las Entradas
class Categoria(models.Model):
	nombre = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True) #slug que vamos a usar para mostrar la direccion absoluta de de cada categoria

	class Meta:
		verbose_name_plural = 'Categorias'

	def __unicode__(self):
		return self.nombre

	@permalink
	def get_absolute_url(self):
		return ('categorias', None, { 'slug': self.slug })

#Clase para las Entradas
class Post(models.Model):
	titulo		= models.CharField(max_length=100, unique=True)
	slug 		= models.SlugField(max_length=100, unique=True) #slug para crear la direccion de cada entrada, este no debe ser repetido
	autor 		= models.CharField(max_length=100)
	contenido	= RichTextField()
	fecha 		= models.DateTimeField(db_index=True, auto_now_add=True)
	estado		= models.CharField(max_length=1, choices=ESTADO)
	categoria 	= models.ManyToManyField(Categoria)
	tags 		= TaggableManager()

	class Meta:
		ordering=['-fecha']
		verbose_name_plural='Entradas'

	def __unicode__(self):
	 	return self.titulo

	@permalink
	def get_absolute_url(self):
		return ('entradas', None, { 'slug': self.slug })