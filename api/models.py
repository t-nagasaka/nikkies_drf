from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.conf import settings


# upload_toのパス作成関数
def upload_avatar_path(instance, filename):
    # 拡張子を取り出し(例：jpgやpng)
    ext = filename.split('.')[-1]
    # 保存先のパスを作成して返却
    return '/'.join([
        'avatars',
        str(instance.userProfile.id)+str(instance.nickName)+str('.')+str(ext)])


# upload_toのパス作成関数
def upload_post_path(instance, filename):
    # 拡張子を取り出し(例：jpgやpng)
    ext = filename.split('.')[-1]
    # 保存先のパスを作成して返却
    return '/'.join([
        'posts',
        str(instance.userPost.id)+str(instance.title)+str('.')+str(ext)])


class UserManager(BaseUserManager):
    # カスタムユーザーを作るが今回はemailへの変更はしない
    def create_user(self, username, password=None):
        user = self.model(username=username)
        user.set_password(password)
        user.save(useing=self._db)
        # ユーザー名とパスワードを設定したユーザーモデルを返却
        return user

    # カスタムユーザー作成時はスーパーユーザーも作成
    def cerate_superuser(self, username, password=None):
        user = self.model(username=username)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # UserManagerをネストする
    objects = UserManager()

    # デフォルトのusernameをemailへオーバーライド
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Diaries(models.Model):
    user_diary = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='user_diary',
                                   on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    display_date = models.DateField()
    picture_01 = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    picture_02 = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    picture_03 = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    picture_04 = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    picture_05 = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'diaries'
        verbose_name_plural = '日記'
        ordering = ('display_date',)

    def __str__(self):
        return f'{str(self.display_date)} {self.title}'


class Pages(models.Model):
    user_page = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='user_page',
                                  on_delete=models.CASCADE)
    history01_display_date = models.ForeignKey('Diaries',
                                               related_name='history01_display_date',
                                               on_delete=models.CASCADE)
    history02_display_date = models.ForeignKey('Diaries',
                                               related_name='history02_display_date',
                                               on_delete=models.CASCADE)
    history03_display_date = models.ForeignKey('Diaries',
                                               related_name='history03_display_date',
                                               on_delete=models.CASCADE)

    class Meta:
        db_table = 'pages'
        verbose_name_plural = 'ページ'
