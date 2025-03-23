from django.shortcuts import render
from flask import Response
from rest_framework import viewsets
from django.db.models import Count
from rest_framework.decorators import action

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def top_liked(self, request):
        posts = Post.objects.annotate(likes_count=Count('post_likes')).order_by('-likes_count')[:5]
        return Response(PostSerializer(posts, many=True).data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get'])
    def most_commented(self, request):
        comments = Comment.objects.annotate(likes_count=Count('comment_likes')).order_by('-likes_count')[:5]
        return Response(CommentSerializer(comments, many=True).data)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
