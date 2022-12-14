from time import timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, request, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic.edit import FormView, CreateView

from .models import User, Post


# from firstapp.models


def my_first_view(request):
    users = User.objects.all()
    posts = Post.objects.all()
    return render(request, 'user_list.html', context={'users': users, 'posts': posts})



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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'post_create.html'

    def get_success_url(self):
        return reverse_lazy('firstapp:post_detail', kwargs={'pk': self.object.id})








