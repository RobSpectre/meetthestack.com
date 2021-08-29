from django.test import TestCase

from sms.models import SmsMessage


class SmsMessageModelTestCase(TestCase):
    def setUp(self):
        self.sms_message = SmsMessage.objects.create(sid="MMxxxx",
                                                     from_number="from",
                                                     to_number="to",
                                                     body="Test.")

    def test_string_representation(self):
        date = self.sms_message.date_created
        body = self.sms_message.body
        self.assertEqual(str(self.sms_message),
                         "{0} - None: {1}".format(date, body))
