from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .sitemaps import PostSitemap
from . import views


app_name = 'blog'

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<str:category>', views.CategoryView, name='category'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit', views.EditPostView.as_view(), name='edit_post'),
    path('<slug:slug>/delete', views.DeletePostView.as_view(), name='delete_post'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

