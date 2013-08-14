# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class UserModels(User):
    shop_name = models.CharField(verbose_name=_('Наименование магазина'), max_length=50)
    shop_description = models.TextField(verbose_name=_('Описание'), max_length=400)
