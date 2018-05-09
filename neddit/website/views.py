from django.shortcuts import render, get_object_or_404
from django.views import generic


class BaseView(generic.TemplateView):
    template_name = 'website/base.html'


class LandingView(BaseView):
    template_name = 'website/landing.html'


class IndexView(BaseView):
    template_name = 'website/index.html'


class FaqView(BaseView):
    template_name = 'website/faq.html'


def view_subneddit(request, subneddit):
    context = {
        'subneddit_code': subneddit.upper(),
    }
    return render(request, 'website/subneddit.html', context)
