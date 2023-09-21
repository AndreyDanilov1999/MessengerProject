from django.forms import ModelForm

from chat.models import Chat


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = 'room_name', 'type', 'participants'

