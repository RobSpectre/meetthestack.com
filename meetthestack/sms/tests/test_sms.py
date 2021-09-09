from django.test import TestCase
from django.test import Client
from django.test import override_settings

from twilio.request_validator import RequestValidator


class TwilioTestClient(Client):
    def sms(self, body, path="/sms/", to="+15558675309", from_="+15556667777",
            extra_params=None):
        params = {"MessageSid": "SMtesting",
                  "AccountSid": "ACxxxxx",
                  "To": to,
                  "From": from_,
                  "Body": body,
                  "Direction": "inbound",
                  "FromCity": "BROOKLYN",
                  "FromState": "NY",
                  "FromCountry": "US",
                  "FromZip": "55555"}

        if extra_params:
            for k, v in extra_params.items():
                params[k] = v

        HTTP_HOST = "example.com"
        validator = RequestValidator("yyyyyyyy")
        absolute_url = "http://{0}{1}".format(HTTP_HOST,
                                              path)
        signature = validator.compute_signature(absolute_url,
                                                params)

        return self.post(path, params,
                         HTTP_X_TWILIO_SIGNATURE=signature,
                         HTTP_HOST=HTTP_HOST)

    def call(self, to, path="/voice/", from_="+15556667777",
             extra_params=None):
        params = {"CallSid": "CAtesting",
                  "AccountSid": "ACxxxxx",
                  "To": to,
                  "From": from_,
                  "Direction": "inbound",
                  "FromCity": "BROOKLYN",
                  "FromState": "NY",
                  "FromCountry": "US",
                  "FromZip": "55555"}

        if extra_params:
            for k, v in extra_params.items():
                params[k] = v

        HTTP_HOST = "example.com"
        validator = RequestValidator("yyyyyyyy")
        absolute_url = "http://{0}{1}".format(HTTP_HOST,
                                              path)
        signature = validator.compute_signature(absolute_url,
                                                params)

        return self.post(path, params,
                         HTTP_X_TWILIO_SIGNATURE=signature,
                         HTTP_HOST=HTTP_HOST)


@override_settings(TWILIO_AUTH_TOKEN="yyyyyyyy",
                   ALLOWED_HOSTS=['example.com'])
class TwilioTestCase(TestCase):
    def setUp(self):
        self.client = TwilioTestClient()

    def assert_twiml(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Response>")


@override_settings(TWILIO_AUTH_TOKEN="yyyyyyyy",
                   ALLOWED_HOSTS=['example.com'])
class RouterTestCase(TwilioTestCase):
    def test_sms_extra_parameters(self):
        response = self.client.sms("Test.")

        self.assert_twiml(response)
