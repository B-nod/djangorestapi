from dataclasses import fields
import json
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description','file', 'poster','poster_id', 'created', 'comments']
    
    def get_comments(self, post):
        return Comment.objects.filter(post=post).values()

    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment']