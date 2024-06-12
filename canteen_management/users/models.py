from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .managers import CustomUserManager
# To make email primary field for user. Username field removed.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    somaiya_id = models.CharField(_('somaiya id'),validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')],unique=True, max_length=10, blank=True, null=True, default=None)
    profile_pic = models.ImageField(upload_to="profile_pics/", default = 'profile_pics/blank-profile-pic.jpg')
    image_url = models.URLField(_('image URL'), blank=True, null=True)
    REQUIRED_FIELDS = [] 
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, **kwargs):
        self.somaiya_id = self.somaiya_id or None
        super().save(**kwargs)

