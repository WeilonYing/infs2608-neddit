from django.views import generic


class BaseView(generic.TemplateView):
    template_name = 'website/base.html'


class LandingView(BaseView):
    template_name = 'website/landing.html'


class IndexView(BaseView):
    template_name = 'website/index.html'


class FaqView(BaseView):
    template_name = 'website/faq.html'
