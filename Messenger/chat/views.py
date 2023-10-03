import datetime
import json
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from chat.models import *
from chat.forms import *


def e_handler500(request):
    context = RequestContext(request)
    response = render('500.html', context)
    response.status_code = 500
    return response


def profile(request, pk):
    # Get instances of CustomUser
    user_pk = get_object_or_404(CustomUser, user=pk)
    user_2 = get_object_or_404(CustomUser, user=request.user)

    # Фильтруем чаты, где залогиненный юзер является автором или участником
    user_chat = Chat.objects.filter(Q(author=user_2.user) | Q(participants=user_2.user))
    print(user_chat)
    # далее фильтруем два сценария чата и через условие подставляем в переменную chat нужное значение
    chat_user_2 = user_chat.filter(author=user_pk.user, participants=user_2.user).first()
    print('user_2', chat_user_2)
    chat_user_pk = user_chat.filter(author=user_2.user, participants=user_pk.user).first()
    print('user_pk', chat_user_pk)
    if chat_user_2:
        chat = chat_user_2
    elif chat_user_pk:
        chat = chat_user_pk
    else:
        chat = None
    return render(request, 'profile.html', {
        'user_pk': user_pk,
        'user_2': user_2,
        'chat': chat,
    })


def edit_profile(request, pk):
    user = CustomUser.objects.get(user=request.user)

    return render(request, 'edit_profile.html', {
        'user': user,
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


def my_chats(request):
    # Check if the current user is the author of the chat
    chat_as_author = Chat.objects.filter(author=request.user)
    print(chat_as_author)
    # Check if the current user is a participant in the chat
    chat_as_participant = Chat.objects.filter(participants=request.user)
    print(chat_as_participant)
    return render(request, 'chat/my_chats.html', {
        'chats_1': chat_as_author,
        'chats_2': chat_as_participant,
    })


def room(request, room_name):
    # Check if the current user is the author of the chat
    chat_as_author = Chat.objects.filter(author=request.user, room_name=room_name).first()

    # Check if the current user is a participant in the chat
    chat_as_participant = Chat.objects.filter(participants=request.user, room_name=room_name).first()

    if chat_as_author:
        author = request.user
        chats = chat_as_author
    elif chat_as_participant:
        author = chat_as_participant.author
        chats = chat_as_participant
    else:
        print('nothing')
        # Handle the case where neither author nor participant
        return render(request, '403.html')

    messages = Message.objects.filter(room_name=chats.id)[0:25]  # Fetch messages
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': author,
        'messages': messages,
        'chats': chats,
    })


def chat_room(request, room_name):
    user = request.user
    chat = get_object_or_404(Chat, room_name=room_name)
    members = list(chat.participants.all())
    members_name = list(chat.participants.all().values_list('username', flat=True))
    author = chat.author

    if user == author or user in members:
        messages = Message.objects.filter(room_name=chat.id)[0:25]
        return render(request, 'chat/chat_room.html', {
            'author': author,
            'user': user,
            'room_name': room_name,
            'chat': chat,
            'messages': messages,
            'participants': members,
        })
    else:
        members = list(chat.participants.all().values_list('id', flat=True))
        return render(request, 'chat/chat_room_join.html', {
            'room_name': room_name,
            'chats': chat,
            'user': user,
            'participants': members,
        })


def chat_room_edit(request, room_name):
    chat = get_object_or_404(Chat, room_name=room_name)
    members = list(chat.participants.all())
    members_id = list(chat.participants.all().values_list('id', flat=True))
    return render(request, 'chat/chat_room_options.html', {
        'room_name': room_name,
        'chats': chat,
        'participants': members,
        'part_id': members_id,
    })


def create_chat_room(request):
    return render(request, 'chat/room_create.html', {

    })
