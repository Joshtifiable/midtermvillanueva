from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm
from datetime import datetime

# Create your views here.

def index(request):
    #return HttpResponse('Hello World!')
    context = {}
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, 'index.html', context)

def help(request):
    return HttpResponse('This is the help page')

def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponse('Post updated')
        context['form'] = forms
        render(request, 'update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'update.html', context)

def comment(request, post_id):
    context = {}
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'comment.html', context)
        #return HttpResponse('Question created')
        #context['form'] = form
        #render(request, 'create.html', context)
    else:
        context['form'] = PostModelForm(initial={"date_created": datetime.now()})
    return render(request, 'detail.html', context)

def create(request):
    context = {}
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'create.html', context)
        #return HttpResponse('Question created')
        #context['form'] = form
        #render(request, 'create.html', context)
    else:
        context['form'] = PostModelForm(initial={"date_created": datetime.now()})
    return render(request, 'create.html', context)
