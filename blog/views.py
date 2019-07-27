from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

def about(request):
    return render(request, 'about.html')

def home(request):
    blogs = Blog.objects #쿼리셋: 전달받은 객체 #메소드: 쿼리셋에게 기능을 표시해주는 것
    blog_list = Blog.objects.all()

    paginator = Paginator(blog_list,3)

    page = request.GET.get('page')
    
    posts = paginator.get_page(page)

    return render(request,'home.html', {'blogs':blogs, 'posts':posts})

    #쿼리셋과 메소드 형식 - 모델.쿼리셋(object).메소드

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id) #클래스와 몇번 객체인지의 pk값 이 두 가지 인자를 받음

    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수!
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))