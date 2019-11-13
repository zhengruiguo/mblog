from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())
#    post_lists = list()
#    for count,post in enumerate(posts):
#        post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
#        post_lists.append("<small>"+str(post.body)\
#        +"</small><br><br>")
#    return HttpResponse(post_lists)
