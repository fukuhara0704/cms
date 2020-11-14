from django.views import generic
from .models import Post
from django.http import JsonResponse


class PostList(generic.ListView):
    model = Post

def ajax_post_add(request):
    title = request.POST.get('title')
    post = Post.objects.create(title=title)
    d = {
        'title': post.title,
    }
    return JsonResponse(d)

def ajax_post_search(request):
    keyword = request.GET.get('title')

    # 検索キーワードがあればそれで絞り込み、なければ全ての記事
    # JSONシリアライズするには、Querysetをリストにする必要あり
    if keyword:
        title_list = [post.title for post in Post.objects.filter(title__icontains=keyword)]  # タイトルにキーワードを含む。大文字小文字の区別なし
    else:
        title_list = [post.title for post in Post.objects.all()]

    d = {
        'title_list': title_list,
    }
    return JsonResponse(d)