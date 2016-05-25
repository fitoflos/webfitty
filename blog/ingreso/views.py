from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
def post_create(request):
    context = {
        "title" : "create"
    }
    return render (request, "index.html", context)

def post_detail(request, id= None):
    #instance = Post.objects.get(id=2)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title" : "details",
        "instance" : instance,
    }
    return render (request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title" : "Lista"
    }
    return render (request, "index.html", context)

def post_update(request):
    context = {
        "title" : "update"
    }
    return render (request, "index.html", context)

def post_delete(request):
    context = {
        "title" : "delete"
    }
    return render (request, "index.html", context)
