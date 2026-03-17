from blog import views as blog_views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', blog_views.blog, name='home'),
    path('example/', blog_views.example, name='example'),
]
