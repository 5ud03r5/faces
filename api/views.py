from django.contrib.auth.decorators import permission_required
from .serializers import CommentSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from faces_app.models import Comment, Post
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import viewsets



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['POST', 'GET'], serializer_class=CommentSerializer)
    def add_comment(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=self.get_object(), owner=self.request.user.profile)
            return Response(serializer.data)



    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.profile)

    



