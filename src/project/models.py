from django.db import models
from base.models import TimeModel
from repos.models import TemplateRepo

# Create your models here.


class Project(TimeModel):
    name = models.CharField(max_length=100, verbose_name="项目名称")
    template = models.ForeignKey(TemplateRepo, on_delete=models.DO_NOTHING, verbose_name="模板")
