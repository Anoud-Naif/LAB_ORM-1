from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Blog

# Create your views here.






def add_post_view(request: HttpRequest):

    if request.method == "POST":
        read_blog_item = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"])
        read_blog_item.save()

        return redirect("blogApp:home_view")

    return render(request, "blogApp/add_post.html")




def read_blog_view(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "blogApp/read_blog.html", {"blogs" : blogs})