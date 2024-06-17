from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField('Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(max_length=30, verbose_name='Текст')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Картинка'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        ordering = ('pub_date',)
        default_related_name = 'posts'

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField(max_length=20, verbose_name='Текст')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return (f'Пользователь {self.author} прокомментировал пост '
                f'"{self.post}": {self.text}')


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='user_prevent_self_follow'
            )
        ]

    def __str__(self):
        return (f'{self.user}) подписан на {self.following}')
