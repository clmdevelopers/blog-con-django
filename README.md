Blog con Django
===============

Blog simple realizado con Django:
- feed
- paginación
- páginas estáticas
- archivos
- tags
- comentarios

utlizando <a href="https://mariadb.org/" target="_blank">MariaDB</a> como base de datos.

Para utilizar los tags se instala django-taggit <br/>
<code>pip install django-taggit</code>

Además se ha utilizado el un template free Dropetrope, puedes verlo y descargarlo en el siguiente enlace http://html5up.net/dopetrope/ 

Para los comentarios se usamos Disqus, las instrucciones en el siguiente enlace https://gist.github.com/lavaldi/5338889

Se ha integrado <a href="http://ckeditor.com/" target="_blank">CKEDITOR</a> al admin de Django para utilizarlo en la edición de los post.
- Se instala con el siguiente comando <code>sudo pip install django-ckeditor</code> ó <code>easy_install django-ckeditor</code>
- Una ves que lo tenemos instalado lo siguiente que necesitamos hacer es registrar nuestra aplicación en nuestro archivo settings.py asi:<br/>
<code>
CKEDITOR_UPLOAD_PATH = "/media/" #Carpeta donde se van a subir archivos <br/>
INSTALLED_APPS = ( <br/>
'ckeditor', # Agregamos a nuestras aplicaciones <br/>
 )
</code>

- Luego vemos que la carpeta "static" tenga todos los permisos y ejecutamos en comando:<br/>
<code>sudo ./manage.py collectstatic</code>

- Y por último, agregamos la URL de CKEDITOR en urls.py:<br/>
<code>(r'^ckeditor/', include('ckeditor.urls')),</code>

PD: Faltan arreglar búsqueda y las vistas por categoría.
