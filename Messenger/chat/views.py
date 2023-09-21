import datetime
import json


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView

from chat.models import *
from chat.forms import *


class ChatCreate(CreateView):
    model = Chat
    form_class = ChatForm
    template_name = 'chat_create.html'
    context_object_name = 'chat_create'

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = self.request.user
        return super().form_valid(form)


def profile(request, pk):
    user_pk = CustomUser.objects.get(user=pk) # объект юзера по запросу
    user_2 = CustomUser.objects.get(user=request.user) # объект залогиненного юзера
    profile_verify = list(Chat.objects.filter(author_id=request.user.id, room_name=user_pk).values_list('author__username', flat=True))
    profile_verify_too = ''.join(map(str, profile_verify))

    if profile_verify_too:
        user = CustomUser.objects.get(user=pk)
        chats = Chat.objects.get(author_id=request.user.id, room_name=user)

        print('1')
    elif Chat.objects.filter(author_id=pk, room_name=user_2):
        chats = Chat.objects.get(author_id=pk, room_name=user_2)
        user = CustomUser.objects.get(user=request.user.id)
        print('2')
    else:
        chats = []
        user = CustomUser.objects.get(user=request.user)
        print('3')
    return render(request, 'profile.html', {
        'user_pk': user_pk,
        'user': user,
        'user_2': user_2,
        'chats': chats,
    })


def index(request):
    username = request.user.id
    users = CustomUser.objects.all()
    chats = Chat.objects.all()
    return render(request, 'index.html', {
        'username': username,
        'chats': chats,
        'users': users,
    })


def room(request, room_name):
    # выполняется если в комнату попадает автор чата
    if Chat.objects.filter(author_id=request.user.id, room_name=room_name):
        author = User.objects.get(username=request.user) # экземпляр юзера
        chats = Chat.objects.get(author_id=request.user.id, room_name=room_name) # экземпляр чата
    # выполняется если в комнату попадает участник чата
    elif Chat.objects.filter(participants__username=request.user):
        author_chat = list(Chat.objects.filter(room_name=room_name).values_list('author__username', flat=True))
        print(' '.join(map(str, author_chat)))
        author = User.objects.get(username=''.join(map(str, author_chat))) # экземпляр юзера
        member = list(Chat.objects.get(room_name=room_name).participants.all().values_list('id', flat=True))
        chats = Chat.objects.get(participants__id=''.join(map(str, member))) # экземпляр чата
    else:
        print('nothing')
    messages = Message.objects.filter(room_name=chats.id)[0:25] # вывод сообщений из бд
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': author,
        'messages': messages,
        'chats': chats,
    })

