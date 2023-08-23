from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('category/<slug:name>/', views.category_posts, name='category_posts'),
    path('post/<slug:post_slug>/', views.post_detail, name='post_detail'),


]