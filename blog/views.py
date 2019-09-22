from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request,"home.html")

def greet(request,name):
    return HttpResponse(f"Hello {name}! How are you doing")

def post_page(request,post_id):
    print(post_id)
    post = BlogPost.objects.get(pk=post_id)
    return render(request,"post.html",{"selected_post":post})

def all_posts(request):
    all_posts = BlogPost.objects.all()
    return render(request,"allposts.html",{"posts":all_posts})

def create_post(request):

    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = BlogPost.objects.create(title=title,content=content)
        return redirect("/allposts/")

    return render(request,"create_post.html")

def delete_post(request,post_id):
    post = BlogPost.objects.get(pk=post_id)
    post.delete()
    return redirect("/allposts/")

def edit_post(request,post_id):
    post = BlogPost.objects.get(pk=post_id)

    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        
        post.title = title
        post.content = content
        post.save()
        return redirect(f"/post/{post.id}")

    return render(request,"edit_post.html",{"post":post})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        exists = User.objects.filter(username=username).exists()

        if not exists:
            user = User.objects.create_user(username,email,password)
            return HttpResponse("Created User Successfully")

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/allposts/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("Unable to login")
    return render(request,"signin.html")    

def signout(request):
    logout(request)
    return redirect('/')
