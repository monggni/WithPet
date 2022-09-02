from django.shortcuts import render, redirect

# View에 Model(Post 게시글) 가져오기
from .models import Post, Photo


# Create your views here.

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request,'main/index.html')


# blog.html 페이지를 부르는 blog 함수
def blog(request):
     # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴
    return render(request, 'main/blog.html', {'postlist':postlist})


# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})


# spot.html
def spot(request):
    return render(request, 'main/spot.html')

def spot_detail(request):
    return render(request, 'main/spot_detail.html')

def my_page(request):
    return render(request, 'main/mypage.html')

#글쓰기

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')



#삭제기능

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})