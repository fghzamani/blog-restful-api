from django.urls import path
from .views import UserList ,UserDetail,PostList, PostDetail,CommentList,CommentDetail,LogoutApiView


urlpatterns = [
path('users/', UserList.as_view()),
path('users/<int:pk>/', UserDetail.as_view()),
path('posts/', PostList.as_view()),
path('posts/<int:pk>/', PostDetail.as_view()),
path('comments/', CommentList.as_view()),
path('comments/<int:pk>/', CommentDetail.as_view()),
path('logout/', LogoutApiView.as_view()),

]
