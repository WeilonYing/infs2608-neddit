from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import LoginForm, PostForm
from .models import Post, Subneddit
from .utils import create_post, get_comments


class BaseView(generic.TemplateView):
    template_name = 'website/base.html'


class LandingView(BaseView):
    template_name = 'website/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context


class IndexView(BaseView):
    template_name = 'website/index.html'


class FaqView(BaseView):
    template_name = 'website/faq.html'


def view_subneddit(request, sub_id):
    sub_id = sub_id.upper() # subneddit code is always uppercase
    subneddit_obj = Subneddit.objects.get(id=sub_id)
    if not subneddit_obj:
        return HttpResponseNotFound()

    posts = subneddit_obj.post_set.all() # get all posts in this subneddit
    context = {
        'subneddit': subneddit_obj,
        'sidebar': "",
        'posts': posts
    }
    return render(request, 'website/subneddit_posts.html', context)


def view_newpost(request, sub_id):
    sub_id = sub_id.upper()
    subneddit_obj = Subneddit.objects.get(id=sub_id)
    if not subneddit_obj:
        return HttpResponseNotFound()

    context = {
        'subneddit': subneddit_obj,
        'sidebar': "",
        'form': PostForm(),
    }
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        title = request.POST['title']
        author = request.user
        content = request.POST['content']
        file = None  # TODO: Add file support #6
        isTextPost = True  # TODO: Add file support #6

        if create_post(sub_id, title, author, content, file, isTextPost):
            return HttpResponseRedirect(
                reverse('website:subneddit', args=(sub_id,)))
        return HttpResponseServerError()

    return render(request, 'website/subneddit_newpost.html', context)

def view_post(request, sub_id, post_id):
    sub_id = sub_id.upper()
    subneddit_obj = Subneddit.objects.get(id=sub_id)
    if not subneddit_obj:
        return HttpResponseNotFound()

    post_obj = Post.objects.get(id=post_id)
    comments = get_comments(post_obj)
    print(comments)
    context = {
        'subneddit': subneddit_obj,
        'sidebar': "",
        'post': post_obj,
        'comments': comments
    }
    return render(request, 'website/subneddit_viewpost.html', context)
