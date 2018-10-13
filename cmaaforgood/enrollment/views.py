# -*- coding: utf-8 -*-
from oauth2client.client import SignedJwtAssertionCredentials
from __future__ import unicode_literals
from __future import print_function
import gspread
import pandas as pd
import json

from django.shortcuts import render

def index():
        return HttpResponse("Hello World")
