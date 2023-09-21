from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView

from accounts.forms import SignUpForm
from chat.models import CustomUser


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        custom = CustomUser.objects.create(user=user, id=user.id)
        custom.save()
        return super().form_valid(form)
