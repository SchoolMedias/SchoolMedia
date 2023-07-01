from django.db import models


class User(models.Model):
    # 头像
    profile = models.ImageField
    # 用户名
    username = models.CharField(max_length=20)
    # 账号
    number = models.CharField(max_length=20,unique=True)
    #密码
    password = models.CharField(max_length=20)
    # 手机号
    telephone = models.CharField(max_length=11,unique=True)
    #注册时间
    data=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Manager(models.Model):
    number = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.id



# 套模板
"""class UserManage(BaseUserManager):
    # _表示是受保护的，只能在这个类中可以调用
    def _create_user(self,telephone,username,password,**kwargs):
        if not telephone:
            raise ValueError('必须要传递手机号')
        if not password:
            raise ValueError('必须要输入密码')
        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

	# 创建普通用户
    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username,password=password,**kwargs)

    # 创建超级用户
    def create_superuser(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)


class User(AbstractUser):
    #用户名，邮箱，密码，创建时间，权限等  内置模型自带
    # 头像
    profile = models.ImageField
    # 账号
    number = models.CharField(max_length=20)
    # 手机号
    telephone = models.CharField(max_length=11,unique=True)

    # 我们在使用authenticate的时候，默认传入的就好似username和password字段
    # 现在我们设置了这个属性的值，那么再使用authenticate的时候，就会使用我们设定的字段
    USERNAME_FIELD = 'telephone'
    objects = UserManage()
"""