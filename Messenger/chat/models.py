from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Chat(models.Model):
    PRIVATE_CHAT = 'CHAT'
    CHAT_ROOM = 'ROOM'
    CATEGORY_CHOICES = (
      (PRIVATE_CHAT, 'CHAT'),
      (CHAT_ROOM, 'ROOM')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    type = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default=PRIVATE_CHAT)
    room_name = models.CharField(max_length=255, unique=True)
    participants = models.ManyToManyField(User, related_name='participants')

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return f'/messenger/{self.room_name}'


class Message(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messages')
    room_name = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.content
