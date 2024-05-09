from django.urls import path, include
from rest_framework import routers
from .views import (
    ClientViewSet, create_client, update_client, delete_client,
    MailViewSet, create_mail, update_mail, delete_mail, mail_statistics, mail_detail_statistics,
    MessageViewSet, create_message, update_message, delete_message,
    TagViewSet, create_tag, update_tag, delete_tag,
    CodeViewSet, create_code, update_code, delete_code
)

router = routers.DefaultRouter()
router.register(r'api/mail', MailViewSet)
router.register(r'api/client', ClientViewSet)
router.register(r'api/message', MessageViewSet)
router.register(r'api/tag', TagViewSet)
router.register(r'api/code', CodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/mail/', create_mail, name='create_mail'),
    path('api/mail/<int:mail_id>/', update_mail, name='update_mail'),
    path('api/mail/<int:mail_id>/', delete_mail, name='delete_mail'),
    path('api/stats/mail/', mail_statistics, name='mail_statistics'),
    path('api/stats/mail/<int:mail_id>/', mail_detail_statistics, name='mail_detail_statistics'),
    path('api/client/', create_client, name='create_client'),
    path('api/client/<int:client_id>/', update_client, name='update_client'),
    path('api/client/<int:client_id>/', delete_client, name='delete_client'),
    path('api/message/', create_message, name='create_message'),
    path('api/message/<int:message_id>/', update_message, name='update_message'),
    path('api/message/<int:message_id>/', delete_message, name='delete_message'),
    path('api/tag/', create_tag, name='create_tag'),
    path('api/tag/<int:tag_id>/', update_tag, name='update_tag'),
    path('api/tag/<int:tag_id>/', delete_tag, name='delete_tag'),
    path('api/code/', create_code, name='create_code'),
    path('api/code/<int:code_id>/', update_code, name='update_code'),
    path('api/code/<int:code_id>/', delete_code, name='delete_code'),
]
