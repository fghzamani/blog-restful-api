from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post ,Comment,Category

class UserSerializer(serializers.ModelSerializer):
    # name should be the same as  it's related_name arguman
    #برای این که پستای ی هر یوزر رو هم با اطلاعات یوزر نشون بده
    posts = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True,read_only=True) ### برای این که ببینم هر یوزر چه کتگوری هایی داره یا ایجاد کرده
    class Meta:
        model = User
        fields = ['id','username','posts','categories']

class PostSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    categories = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Post 
        fields =['id','title','body','owner','categories']

class CommentSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True) # اطلاعات هر کامنت و با اطلاعات یوزر نشون بده
    class Meta:
        model = Comment
        fields =['id','body','owner','post','comments']

class CategorySerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True) # اطلاعات هر کامنت و با اطلاعات یوزر نشون بده
    class Meta:
        model = Category
        fields =['id','name','owner','post','comments']
