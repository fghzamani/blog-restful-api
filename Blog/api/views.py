from django.shortcuts import render
from .serializers import UserSerializer,PostSerializer,CommentSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Post,Comment,Category
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    permission_class =[permissions.IsAuthenticated]
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self,serializer):
        serializer.save(owner = self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class =[permissions.IsAuthenticated,IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveAPIView):
    permission_class =[permissions.IsAuthenticated,IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CommentSerializer
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CommentSerializer

class LogoutApiView(generics.GenericAPIView):
    permission_class = [permissions.IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response(data = {"massage":f"Goodbye{request.user.username}"})

# class PostListView(PermissionRequiredMixin, ListView):
#     model = Post
#     permission_required = ['api.can_hide_post',]