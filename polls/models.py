from django.db import models


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()


class Code(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()


class Mail(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)  # Связь с моделью Tag
    code = models.ForeignKey('Code', on_delete=models.CASCADE)  # Связь с моделью Code
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    send_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    mail_id = models.ForeignKey(Mail, on_delete=models.CASCADE)  # Связь с моделью Mail
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE)  # Связь с моделью Client


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)  # Связь с моделью Tag
    code = models.ForeignKey('Code', on_delete=models.CASCADE)  # Связь с моделью Code
    time_zone = models.CharField(max_length=50)