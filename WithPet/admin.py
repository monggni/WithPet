from django.contrib import admin

# Register your models here.

# 게시글(Post) Model을 불러옵니다
from .models import Post, Photo


##이거는 이미지 222ver
class PhotoInline(admin.TabularInline):
    model=Photo

class PostAdmin(admin.ModelAdmin):
    inlines=[PhotoInline, ]


# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post, PostAdmin)