
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class MyUserManager(BaseUserManager):
    def create_user(self, email,  name, tel_phone, date_of_birth=None, password=None): #創建普通用戶的方法
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            name=name,
            tel_phone=tel_phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password, name, tel_phone):  #創建超級用戶的方法
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            name=name,
            tel_phone=tel_phone,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):    #自定義用戶表，創建需要的字段， 需要繼承PermissionsMixin才能生成權限和用戶的關聯
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    name = models.CharField(max_length=32, default='tan', null=False)
    tel_phone = models.CharField(max_length=32, default=18)
    age = models.SmallIntegerField(default=18)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tel_phone', 'date_of_birth']   #指定創建用戶需要填寫的字段

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email


class HostList(models.Model):
    hostname = models.CharField(verbose_name='主机名', max_length=64)
    ipaddr = models.CharField(verbose_name='ip地址', max_length=64)
    status_choice = ((0, '启用'), (1, '禁用'))
    status = models.SmallIntegerField(choices=status_choice)
    role = models.ForeignKey('Roles', on_delete=models.CASCADE)
    group = models.ManyToManyField('dev_group')
    isp = models.ForeignKey('ISP', on_delete=models.CASCADE)
    remarks = models.CharField(verbose_name='备注', max_length=512, blank=True, null=True)
    def __str__(self):
        return self.hostname

class Roles(models.Model):
    name = models.CharField(verbose_name='设备角色', max_length=64)
    describe = models.CharField(verbose_name='角色描述', max_length=512)
    def __str__(self):
        return self.name

class dev_group(models.Model):
    name = models.CharField(verbose_name='设备组', max_length=64)
    describe = models.CharField(verbose_name='设备组描述', max_length=512)
    def __str__(self):
        return self.name

class ISP(models.Model):
    name = models.CharField(verbose_name='运营商', max_length=64)

    def __str__(self):
        return self.name