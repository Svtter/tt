from django.db import models
from base.models import TimeModel

# Create your models here.


class TemplateRepos(TimeModel):
    name = models.CharField(max_length=100, verbose_name="名称")
    repos = models.CharField(max_length=100, verbose_name="仓库地址")
    content = models.TextField("内容", blank=True, null=True)
