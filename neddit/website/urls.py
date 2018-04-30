from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('landing', views.LandingView.as_view(), name='landing')
]
