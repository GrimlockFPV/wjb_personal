from . import views
from django.urls import include

from django.urls import path

app_name = 'blog'

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail, name="post_detail"),
    path("category/<str:cats>/", views.CategoryList, name="category"),
]

