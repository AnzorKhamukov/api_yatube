from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name: str = 'Group'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='для текста')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария',
    )
    created = models.DateTimeField(
        verbose_name='Дата комментария',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.text[:15]
