from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .import serializers
from .models import User, Diary, Page


# 新規ユーザー作成処理の作成
# 作成のみのためCreateAPIViewを使用
class CreateUserView(generics.CreateAPIView):
    # 対象のserializerを指定(必須)
    serializer_class = serializers.UserSerializer
    # JWTの認証を誰でも可に上書き
    permission_classes = (AllowAny,)
    serializer = serializers.UserSerializer


# ログインしているユーザーの情報を返す
class UserEditViewSet(viewsets.ModelViewSet):
    # すべてのプロフィールを取得
    queryset = User.objects.all()
    # 対象のserializerを指定(必須)
    serializer_class = serializers.UserSerializer

    # オーバーライドメソッド
    def get_queryset(self):
        # ログインしているユーザーの情報を取得して返却
        return self.queryset.filter(username=self.request.user)


# ログインしているユーザーの情報を返す
class MyProfileListView(generics.ListAPIView):
    # すべてのプロフィールを取得
    queryset = User.objects.all()
    # 対象のserializerを指定(必須)
    serializer_class = serializers.UserSerializer

    # オーバーライドメソッド
    def get_queryset(self):
        # ログインしているユーザーの情報を取得して返却
        return self.queryset.filter(username=self.request.user)


class DiaryViewSet(viewsets.ModelViewSet):
    # すべての投稿を取得
    queryset = Diary.objects.all()
    # 対象のserializerを指定(必須)
    serializer_class = serializers.DiarySerializer
    # オーバーライドメソッド

    def perform_create(self, serializer):
        # ログインしているユーザーの情報を取得して保存
        # print(self.request.data['title'])
        serializer.save(user_diary=self.request.user)

    # オーバーライドメソッド
    def get_queryset(self):
        get_date = self.request.query_params.get('display_date')
        post_date = self.request.data
        if get_date:
            date = get_date
        else:
            date = post_date['display_date']
        # ログインしているユーザーの情報を取得して返却
        return self.queryset.filter(user_diary=self.request.user).filter(display_date=date)


class PageViewSet(viewsets.ModelViewSet):
    # すべての投稿を取得
    queryset = Page.objects.all()
    # 対象のserializerを指定(必須)
    serializer_class = serializers.PageSerializer

    def get_queryset(self):
        return self.queryset.filter(user_page=self.request.user)

    # オーバーライドメソッド
    def perform_create(self, serializer):
        # ログインしているユーザーの情報を取得して保存
        serializer.save(user_page=self.request.user)
