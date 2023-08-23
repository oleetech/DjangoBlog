from django.shortcuts import render, get_object_or_404

from .models import Category,Post

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request,'blog.html',{'categories': categories})

def category_posts(request, name):
    category = Category.objects.get(name=name)

    posts = Post.objects.filter(category=category)
    
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    category = post.category  # Assuming 'category' is the ForeignKey relationship field
    related_posts = Post.objects.filter(category=category)
    return render(request, 'post_detail.html', {'post': post, 'category': category, 'related_posts': related_posts})


