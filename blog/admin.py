from django.contrib import admin
from blog.models import Post, Categoria

class AdminEntrada(admin.ModelAdmin):
	list_display 		= ('titulo', 'autor', 'fecha', 'estado')
	prepopulated_fields = {"slug": ("titulo",)}
	list_filter 		= ('titulo', 'fecha')
	ordering 			= ('-fecha',)
	search_fields 		= ('titulo','texto')
	actions 			= ['publicar_post','marcar_como_borrador']

	def publicar_post(self,request,queryset):
		rows_updated	= queryset.update(estado='p')
		if rows_updated==1:
			message_bit = "1 entrada fue"
		else:
			message_bit = "%s entradas fueron" % rows_updated
		self.message_user(request,"%s publicadas exitosamente." % message_bit)
	publicar_post.short_description = "Marcar como publicadas"

	def marcar_como_borrador(self,request,queryset):
		rows_updated	= queryset.update(estado='b')
		if rows_updated==1:
			message_bit = "1 entrada fue"
		else:
			message_bit = "%s entradas fueron" % rows_updated
		self.message_user(request,"%s marcadas como borrador." % message_bit)
	marcar_como_borrador.short_description = "Marcar como borradores"

class AdminCategoria(admin.ModelAdmin):
	list_display		= ('nombre','slug')
		
admin.site.register(Post, AdminEntrada)
admin.site.register(Categoria, AdminCategoria)