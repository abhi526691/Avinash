from django.shortcuts import render
from pytrends.request import TrendReq
import pytrends
import pandas as pd
trendshow = TrendReq(hl='en-US', tz=360)
# Create your views here.

def index(request):
    all_keywords = ['insurance']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()
    # print(data['insurance']['rising']['query'])
    li = []
    for kw in all_keywords:
        # print(data[kw]['rising']['query'].head(50))
        li.append(data[kw]['rising']['query'])	
        # print(data[kw]['rising']['query'].head(50))
    context = {'li' : data['insurance']['rising']['query']}
    return render(request, 'index.html', context)

def finance(request):
    all_keywords = ['finance']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()
    # print(data['insurance']['rising']['query'])
    li = []
    for kw in all_keywords:
        # print(data[kw]['rising']['query'].head(50))
        li.append(data[kw]['rising']['query'])	
        # print(data[kw]['rising']['query'].head(50))
    context = {'li' : data['finance']['rising']['query']}
    return render(request, 'finance.html', context)

def medical(request):
    all_keywords = ['medical']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()
    # print(data['insurance']['rising']['query'])
    li = []
    for kw in all_keywords:
        # print(data[kw]['rising']['query'].head(50))
        li.append(data[kw]['rising']['query'])	
        # print(data[kw]['rising']['query'].head(50))
    context = {'li' : data['medical']['rising']['query']}
    return render(request, 'medical.html', context)

def loan(request):
    all_keywords = ['loan']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()
    # print(data['insurance']['rising']['query'])
    li = []
    for kw in all_keywords:
        # print(data[kw]['rising']['query'].head(50))
        li.append(data[kw]['rising']['query'])	
        # print(data[kw]['rising']['query'].head(50))
    context = {'li' : data['loan']['rising']['query']}
    return render(request, 'loan.html', context)
