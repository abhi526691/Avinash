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
