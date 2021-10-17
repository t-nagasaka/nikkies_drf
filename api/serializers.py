from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Diaries, Pages


class UserSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'img', 'created_at', 'updated_at')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class DiarySerializer(serializers.ModelSerializer):
    # Djangoの表記が細かいため。年月日に指定
    display_date = serializers.DateTimeField(format='%Y-%m-%d')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = Diaries
        fields = ('user_diary', 'title', 'text', 'display_date',
                  'picture_01', 'picture_02', 'picture_03', 'picture_04', 'picture_05',
                  'create_at', 'updated_at')
        extra_kwargs = {'display_date': {'read_only': True}}


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = ('user_page', 'history01_display_date',
                  'history02_display_date', 'history03_display_date')
        extra_kwargs = {'history01_display_date': {'read_only': True},
                        'history02_display_date': {'read_only': True},
                        'history03_display_date': {'read_only': True}}
