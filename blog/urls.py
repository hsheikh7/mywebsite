
from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'index'),
    path('<int:pid>', blog_single, name = 'single'),
    path('category/<str:cat_name>', blog_category, name = 'category'),
    path('tag/<str:tag_name>', blog_category, name = 'tag'),
    #path('post-<int:pid>', test, name = 'test'),

]
