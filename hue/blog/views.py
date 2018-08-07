from django.shortcuts import render , get_object_or_404 , redirect , get_list_or_404
from .models import *
from .forms import *
from django.contrib import messages
import random
# Create your views here.
def index(request):
    post = Post.objects.all()
    category  = Category.objects.all()
    return render(request , 'blog/index.html' , {'post':post , 'category':category, })

def category(request, pk):
    category_name = Category.objects.filter(id = pk)
    post = Post.objects.filter(category_id = pk)
    return render(request , 'blog/category.html', {'post':post , 'category_name': category_name})

def view(request , pk ):
    ran = random.randint(1 , 10)
    recommended = Post.objects.all()
    post = get_object_or_404(Post , pk=pk)
    return render(request , 'blog/view.html' , {'post':post , 'recommended':recommended , 'ran':ran})

def edit(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if request.method =='POST':
        form = PostForm(request.POST, instance = post)

        if form.is_valid():
            form.save()
            messages.success(request , "Successfully edited")
            return redirect('blog:view' , pk=post.pk)
            
    else:
        form = PostForm(instance = post)
        
    return render(request , 'blog/edit.html' , {'form':form})

def user(request , pk):
    post = get_object_or_404(Author , pk=pk)
    return render(request , 'blog/user.html' , {'post':post})

def author_post(request , pk):
    posts = Post.objects.filter(author_id = pk)
    post= get_list_or_404(posts)
    return render(request , 'blog/author_posts.html' , {'post':post})
