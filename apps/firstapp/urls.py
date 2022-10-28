from django.urls import path
from .views import my_first_view, user_detail

app_name = 'firstapp'

urlpatterns = [
    path('', my_first_view),
    path('user_detail/<int:pk>/', user_detail, name='user_detail'),
    ]