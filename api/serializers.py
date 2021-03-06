from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Diary, Page


class UserSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'created_at', 'updated_at')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # 新規作成時の設定(オーバーライド)
    # validated_dataにはemailとpasswordが格納される(validation OKの場合)
    def create(self, validated_data):
        # models.pyで定義したUser→UserManager→create_userメソッドの実行
        user = get_user_model().objects.create_user(**validated_data)
        return user


class DiarySerializer(serializers.ModelSerializer):
    # Djangoの表記が細かいため。年月日に指定
    display_date = serializers.DateField(format='%Y-%m-%d')
    # created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    # updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Diary
        fields = ('id', 'user_diary', 'title', 'text', 'display_date',
                  'picture_01', 'picture_02', 'picture_03', 'picture_04', 'picture_05',
                  'created_at', 'updated_at')
        extra_kwargs = {'display_date': {'read_only': True}}


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('user_page', 'history01_display_date',
                  'history02_display_date', 'history03_display_date')
