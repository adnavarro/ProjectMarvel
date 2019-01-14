from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from ..models import *
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json