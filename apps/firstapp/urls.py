from django.urls import path
from .views import my_first_view, user_detail, post_detail, PostCreateView

app_name = 'firstapp'

urlpatterns = [
    path('', my_first_view, name='index'),
    path('user_detail/<int:pk>/', user_detail, name='user_detail'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
    path('post_create/', PostCreateView.as_view(), name='post_create')
    ]

#path('', views.post_list, name='post_list'),