from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

        # f'[{self.pk}]self.title}' --> 게시글 번호 추가
