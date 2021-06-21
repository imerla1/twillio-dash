import os
from datetime import datetime
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import logging

TWILIO_ACCOUNT_SID = 'AC7eebcf07728137bd81487c0674254a48'
TWILIO_AUTH_TOKEN = '854ac42e99a7a001d04147113f0c9abf'
logger = logging.getLogger(__name__)
twilio_api = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def fetch_sms():
    return twilio_api.messages.stream()
