# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment


def post_list(request):
    post_list = Post.objects.all()
    
    t=loader.get_template('blog/post_list.html')
    c=Context({'post_list':post_list,})
    #return HttpResponse(post_list)
    return HttpResponse(t.render(c))

def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    me=post.comment_set.all()
    t=loader.get_template('blog/post_detail.html')
    
    if showComments==None:
        c=Context({'post':post,})
        return HttpResponse(t.render(c))
    else:
        c=Context({'post':post,'comments':me})
        return HttpResponse(t.render(c))
    
def post_search(request, term):
    post=Post.objects.filter(body__contains=term)
    t=loader.get_template('blog/post_search.html')
    c=Context({'post_list':post,'search':term})
    return HttpResponse(t.render(c))

def home(request):
    print 'it works'
    t=loader.get_template('base.html')
    c=Context({})
    return HttpResponse(t.render(c)) 
