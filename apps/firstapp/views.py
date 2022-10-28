from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .forms import UserForm
from .models import User


# from firstapp.models


def my_first_view(request):
    users = User.objects.all()
    return render(request, 'user_list.html', context={'users': users})



#@login_required
def user_detail(request, pk):
    user_detail = User.objects.filter(id=pk).first()
    id_not_found = True if user_detail is None else False
    return render(request, 'user_detail.html', {
        'title': 'User Detail',
        'page_active': 'users',
        'id_not_found': id_not_found,
        'pk': pk,
        'user_detail': user_detail,
        'req_user': request.user,
    })

#{% url "firstapp:user_create" %}