from django.db import models

# Create your models here.


# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
     # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(upload_to='images/', blank=True, null=True)
    contents = models.TextField()


     # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname


class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)