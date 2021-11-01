from django.shortcuts import redirect, render

# Create your views here.
from .forms import CommentForm
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'microblog/frontpage.html', {'posts': posts})

def post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post', slug=post.slug)

    else:
        form = CommentForm()

    return render(request, 'microblog/post.html', {'post':post, 'form':form})

