from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import teamdetail, testimonyp, Post
from .forms import CONTACTFORM, CommentForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic


def index(request):
    return render(request, "myapp/onepage-text.html")
def price(request):
    return render(request, "myapp/pricing.html")
def portfolio(request):
    return render(request, "myapp/Portfolio.html")

def main(request):
    return render(request, "main.html")
def blogdetail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, ('thank for contact us'))
        else:
            messages.error(request, ' an error occur in the submitions ')
        return redirect('blogdetail', slug=post.slug)
    else:
        form = CommentForm()
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-created')
    context ={'post' : post, 'form':form}
    return render(request, "myapp/single-post.html", context)


def contact(request):
    form = CONTACTFORM()
    if request.method =='POST':
        form = CONTACTFORM(request.POST, request.FILES )
        if form.is_valid():
            #form= form.save(commit=False)
            form.save()
            messages.success(request, ('thank for contact us'))
        else:
            messages.error(request, ' an error occur in the submitions ')
        return redirect('index')


    return render(request, "myapp/contact.html", {'form':form})
def service(request):
    return render(request, "myapp/service.html")
class TeamView(generic.ListView):
    template_name = 'myapp/team.html'
    context_object_name = 'teams'
    def get_queryset(self):
        return teamdetail.objects.order_by('-created')
def about(request):
    return render(request, "myapp/about.html")
class TestimonyView(generic.ListView):
    template_name = 'myapp/testimony.html'
    context_object_name= 'texty'
    def get_queryset(self):
        return testimonyp.objects.order_by('-created')
class RecentpostView(generic.ListView):
    template_name='myapp/recentpost.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-date_added')[:600]
class BlogView(generic.ListView):
    template_name ='myapp/blog.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-date_added')[:10]
class RecentView(generic.ListView):
    template_name ='myapp/recent.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-date_added')[:16]