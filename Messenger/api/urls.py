from django.urls import include, path
from rest_framework_nested import routers
from api import views

router = routers.SimpleRouter()
router.register(r'chat', views.ChatViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'customuser', views.CustomUserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]