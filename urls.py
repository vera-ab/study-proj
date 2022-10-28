from django.contrib import admin
from django.urls import path, include

#from firstapp.views import my_first_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', my_first_view),
    #path('/', include('firstapp.urls', namespace='firstapp')),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace='accounts')),
    path('', include('apps.firstapp.urls')),

]

#<a href='{% url 'firstapp:user_detail' user_id=user.id %}" >