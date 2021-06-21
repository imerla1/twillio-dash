import os
from datetime import datetime
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import logging

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
logger = logging.getLogger(__name__)
twilio_api = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def fetch_sms():
    return twilio_api.messages.stream()
