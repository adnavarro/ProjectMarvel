from django.contrib.sessions.backends.db import SessionStore
from django.template import Library
from .. models import *
from datetime import datetime, date, time, timedelta
import calendar
from .battles import * 

register = Library()

@register.simple_tag()
def isEventEmpy():
    eventos = Even.objects.all()
    if len(eventos) > 0:
        return False
    else:
        return True
