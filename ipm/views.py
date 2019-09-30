# -*- coding: utf-8 -*-
from io import BytesIO
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import requests
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle  
from reportlab.lib.styles import getSampleStyleSheet  
from reportlab.lib import colors  
from reportlab.lib.pagesizes import letter  
from reportlab.platypus import Table 
import io 
import json
from random import randint
from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal




##Index
@login_required
def index(request):
    
    return render(request, 'ipm/index.html')
    
