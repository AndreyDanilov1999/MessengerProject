"""
URL configuration for Messenger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from chat import views
from django.conf import settings
from django.conf.urls.static import static
from chat.views import e_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messenger/', include('chat.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('my-chats/', views.my_chats, name='my_chats'),
    path('create-room/', views.create_chat_room, name='room_create'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/edit', views.edit_profile, name='edit_profile')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

handler500 = e_handler500