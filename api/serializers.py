from rest_framework import routers, serializers
from faces_app.models import Post, Comment, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['body']

class PostSerializer(serializers.ModelSerializer):
   # comments = CommentSerializer(many=True, source='comment_set')
   # owner = ProfileSerializer(many=False)
    class Meta:
        model = Post
        fields = ['id', 'body', 'picture']
        

