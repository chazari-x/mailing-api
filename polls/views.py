import logging

from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Mail, Client, Message, Tag, Code
from .serializers import MailSerializer, ClientSerializer, MessageSerializer, TagSerializer, CodeSerializer
from rest_framework.viewsets import ModelViewSet


class MailViewSet(ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CodeViewSet(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


@api_view(['POST'])
def create_mail(request):
    serializer = MailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def update_mail(request, mail_id):
    try:
        mail = Mail.objects.get(pk=mail_id)
    except Mail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MailSerializer(mail, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_mail(request, mail_id):
    try:
        mail = Mail.objects.get(pk=mail_id)
    except Mail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    mail.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def mail_statistics(request):
    total_mail = Mail.objects.count()
    total_messages_sent = Message.objects.count()
    status_counts = Message.objects.values('status').annotate(count=Count('id'))
    return Response({
        'total_mails': total_mail,
        'total_messages_sent': total_messages_sent,
        'status_counts': {status['status']: status['count'] for status in status_counts}
    })


@api_view(['GET'])
def mail_detail_statistics(request, mail_id):
    try:
        mail = Mail.objects.get(pk=mail_id)
    except Mail.DoesNotExist:
        return Response({'error': 'Mail does not exist'}, status=404)

    messages_sent = Message.objects.filter(mail_id=mail_id).count()
    status_counts = Message.objects.values('status').annotate(count=Count('id'))

    return Response({
        'mail_id': mail_id,
        'total_messages_sent': messages_sent,
        'status_counts': {status['status']: status['count'] for status in status_counts}
    })


@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def update_client(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_client(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def update_message(request, message_id):
    try:
        message = Message.objects.get(pk=message_id)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MessageSerializer(message, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_message(request, message_id):
    try:
        message = Message.objects.get(pk=message_id)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    message.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_tag(request):
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def update_tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TagSerializer(tag, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_code(request):
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', "PATCH"])
def update_code(request, code_id):
    try:
        code = Code.objects.get(pk=code_id)
    except Code.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CodeSerializer(code, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_code(request, code_id):
    try:
        code = Code.objects.get(pk=code_id)
    except Code.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    code.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)