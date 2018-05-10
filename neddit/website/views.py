from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .forms import LoginForm, PostForm


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


def view_subneddit(request, subneddit):
    context = {
        'subneddit_code': subneddit.upper(),  # subneddit code in upper case
        'sidebar': "",
    }
    return render(request, 'website/subneddit_posts.html', context)


def view_newpost(request, subneddit):
    context = {
        'subneddit_code': subneddit.upper(),
        'sidebar': "",
        'form': PostForm(),
    }
    if request.method == "POST":
        print("Woah!")
        return HttpResponseRedirect(
            reverse('website:subneddit', args=(subneddit,)))

    return render(request, 'website/subneddit_newpost.html', context)
