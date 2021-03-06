from django.urls import path, include

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('landing/', views.LandingView.as_view(), name='landing'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('n/', views.view_subnedditlist, name='subnedditlist'), 
    path('n/<str:sub_id>/', views.view_subneddit, name='subneddit'),
    path('n/<str:sub_id>/new/', views.view_newpost, name='newpost'),
    path('n/<str:sub_id>/<int:post_id>/', views.view_post, name='viewpost'),
    path('n/<str:sub_id>/<int:post_id>/<int:parent_comment_id>/',
            views.post_comment,
            name="postcomment"),
    path('n/<str:sub_id>/<int:post_id>/download/',
            views.post_downloadfile, name='postdownload'),
]
