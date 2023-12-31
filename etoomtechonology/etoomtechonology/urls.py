from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.home.urls')),   
    re_path('', include('applications.entradas.urls')),
    re_path('', include('applications.tareas.urls')),
    # urls de terceros
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)