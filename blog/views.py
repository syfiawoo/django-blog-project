# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from models import Post, Comment
from django.shortcuts import render_to_response


def post_list(request):
    post_list = Post.objects.all()
    
    t=loader.get_template('blog/post_list.html')
    c=Context({'post_list':post_list,})
    #return HttpResponse(post_list)
    return HttpResponse(t.render(c))

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        exclude=['post','author']

    '''def some_body(self):
        return self.body[:60]
    def __unicode__(self):
        return self.body'''


@csrf_exempt
def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    if request.method == 'POST':
        comment = Comment(post=post)
        comment.author=
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()

    me=post.comment_set.all()
    t=loader.get_template('blog/post_detail.html')
    
    if showComments is None:
        c=Context({'post':post,})
        return HttpResponse(t.render(c))
    else:
        c=Context({'post':post,'comments':me,'form' : form})
        return HttpResponse(t.render(c))
    
def post_search(request, term):
    post=Post.objects.filter(body__contains=term)
    t=loader.get_template('blog/post_search.html')
    c=Context({'post_list':post,'search':term})
    return HttpResponse(t.render(c))

def home(request):
    t=loader.get_template('base.html')
    c=Context({})
    return HttpResponse(t.render(c))

@csrf_exempt
def edit_comment(request,id):
    comment=Comment.objects.get(pk=id)
    post_com=Post.objects.get(pk=comment.post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():

            form.save()
        return HttpResponseRedirect(post_com.get_absolute_url())
    else:
        form = CommentForm(initial={'body':comment.body,'author':comment.author})
        form.fields['author'].widget.attrs['readonly'] = True

    return render_to_response('blog/edit_comment.html',locals())

