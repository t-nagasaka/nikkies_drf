from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .import serializers
from .models import User, Diaries, Pages


# 新規ユーザー作成処理の作成
# 作成のみのためCreateAPIViewを使用
class CreateUserView(generics.CreateAPIView):
    # 対象のserializerを指定(必須)
    serializer_class = serializers.UserSerializer
    # JWTの認証を誰でも可に上書き
    permission_classes = (AllowAny,)


# ログインしているユーザーの情報を返す
class UserEditViewSet(viewsets.ModelViewSet):
    # すべてのプロフィールを取得
    queryset = User.objects.all()
    # 対象のserializerを指定(必須)
    serializer_class = serializers.UserSerializer

    # オーバーライドメソッド
    def get_queryset(self, serializer):
        # ログインしているユーザーの情報を取得して返却
        serializer.save(id=self.request.user)


class DiaryViewSet(viewsets.ModelViewSet):
    # すべての投稿を取得
    queryset = Diaries.objects.all()
    # 対象のserializerを指定(必須)
    serializer_class = serializers.DiarySerializer

    # オーバーライドメソッド
    def perform_create(self, serializer):
        # ログインしているユーザーの情報を取得して保存
        serializer.save(user_diary=self.request.user)


class PageViewSet(viewsets.ModelViewSet):
    # すべての投稿を取得
    queryset = Pages.objects.all()
    # 対象のserializerを指定(必須)
    serializer_class = serializers.PageSerializer

    # オーバーライドメソッド
    def perform_create(self, serializer):
        # ログインしているユーザーの情報を取得して保存
        serializer.save(user_page=self.request.user)
