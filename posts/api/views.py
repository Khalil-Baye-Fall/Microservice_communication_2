import json
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

from .models import Post
from .serializers import PostSerializer

def Welcome(request):
    return HttpResponse('I am the Post view!')


class PostApiView(APIView):
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([self.formatPost(p) for p in posts])
    

    def formatPost(self, post):
        
        url = ('http://comment:8001/api/post/%d/comments/' % post.id)
        
       
        
        comments = requests.get(url).json()
            
         
        
        return{
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'comments': comments,
        }


    def post(self, request):
     serializer = PostSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)   
     serializer.save()
     return Response(serializer.data, status=status.HTTP_201_CREATED)