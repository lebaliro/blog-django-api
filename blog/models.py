from django.db import models
from django.contrib.postgres.fields import ArrayField


class BlogModel(models.Model):
    title = models.CharField("Título", max_length=50)
    content = models.TextField("Conteúdo")
    category = models.CharField("Categoria")
    tags = ArrayField(models.CharField(max_length=200), size=5, blank=True, null=True)
