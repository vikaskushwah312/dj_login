from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from post.models import PostForm,Posts


def index(request):
    
    form = PostForm()
    row_data = []
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if form.save():
                row_data = Posts.objects.all()
    print(form)
    return render(request,'index.html',{'form':form,'row_data':row_data})
