# serializers.py

from rest_framework import serializers
from .models import Feedback,Movie,TVShow

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['name','email','feedback_text']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields= ['id','title']

class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields= ['id','title']