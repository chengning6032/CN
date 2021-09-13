from mblog.settings import TEMPLATES
from django.template.loader import get_template
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from datetime import datetime
from .models import Location, Post
# Create your views here.

def index(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())

    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())

            return HttpResponse(html)
    except:
        return redirect('/')

