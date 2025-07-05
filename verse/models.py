from django.db import models

class ListPoem(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Стихотворение")
    author = models.CharField(max_length=100, verbose_name="Автор", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
