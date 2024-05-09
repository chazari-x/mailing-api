from django.utils import timezone
from .models import Mail, Client, Message
from celery import shared_task


@shared_task()
def send_scheduled_mail():
    current_time = timezone.now()
    scheduled_mail = Mail.objects.filter(start_date__lte=current_time, end_date__gt=current_time)

    for mail in scheduled_mail:
        clients = Client.objects.filter(tag=mail.tag, code=mail.code)
        for client in clients:
            messages = Message.objects.filter(mail_id=mail, client_id=client)
            if messages.count() == 0:
                send_message_to_client(client, mail)

    return f"Scheduled mail sent at {current_time}"


def send_message_to_client(client, mail):
    message = Message.objects.create(
        send_date=timezone.now(),  # Установите дату отправки (может потребоваться изменение)
        status="Sent",  # Установите статус сообщения (может потребоваться изменение)
        mail_id=mail,  # Ссылка на рассылку
        client_id=client  # Ссылка на клиента
    )

    message.save()
