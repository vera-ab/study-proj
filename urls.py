from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#from firstapp.views import my_first_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', my_first_view),
    #path('/', include('firstapp.urls', namespace='firstapp')),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace='accounts')),
    path('', include('apps.firstapp.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#<a href='{% url 'firstapp:user_detail' user_id=user.id %}" >