from django.urls import path
from . import views
from .views import Home, MyPost, CreatePost, DetailPost, UpdatePost, DeletePost,\
                   LikeHome, FollowHome, FollowDetail, FollowList, LikeDetail

app_name = 'snsapp'
# app_name = 'register'
urlpatterns = [
   path('', Home.as_view(), name='home'),             
   path('mypost/', MyPost.as_view(), name='mypost'),
   path('detail/<int:pk>', DetailPost.as_view(), name='detail'),  
   path('detail/<int:pk>/update', UpdatePost.as_view(), name='update'),
   path('detail/<int:pk>/delete', DeletePost.as_view(), name='delete'),
   path('create/', CreatePost.as_view(), name='create'),
   path('edit/<int:pk>/', views.edit, name="edit"),
   path('like-home/<int:pk>', LikeHome.as_view(), name='like-home'),
   path('like-detail/<int:pk>', LikeDetail.as_view(), name='like-detail'),
   path('follow-home/<int:pk>', FollowHome.as_view(), name='follow-home'),
   path('follow-detail/<int:pk>', FollowDetail.as_view(), name='follow-detail'),
   path('follow-list/', FollowList.as_view(), name='follow-list'),
]

