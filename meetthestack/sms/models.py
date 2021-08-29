import uuid

from django.db import models

from users.models import User


class SmsMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    sid = models.CharField(max_length=255, db_index=True)
    from_number = models.CharField(max_length=255, db_index=True)
    to_number = models.CharField(max_length=255, db_index=True)
    body = models.TextField(db_index=True)
    related_user = models.ForeignKey(User,
                                     null=True,
                                     related_name="sms_messages",
                                     on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}: {2}".format(self.date_created,
                                       self.related_user,
                                       self.body)
