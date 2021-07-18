from django.shortcuts import render
from pytrends.request import TrendReq
import pytrends
import pandas as pd
trendshow = TrendReq(hl='en-US', tz=360)
# Create your views here.

def index1(request):
    all_keywords = ['insurance']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()

    for kw in all_keywords:	
	    print(data[kw]['rising'].head(50))

def index(request):
    all_keywords = ['insurance']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()

    all_keywordsFinance = ['finance']
    trendshow.build_payload(all_keywordsFinance, cat=0, timeframe='today 1-m', geo='US')
    data1 = trendshow.related_queries()

    context = {'li' : data['insurance']['rising']['query'], 'value' : data['insurance']['rising']['value'], 'financeQuery' : data1['finance']['rising']['query'], 'financeValue' : data1['finance']['rising']['value'] }
    return render(request, 'index.html', context)




def medical(request):
    all_keywords = ['medical']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()

    all_keywords = ['loan']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data1 = trendshow.related_queries()

    context = {'li' : data['medical']['rising']['query'], 'value' : data['medical']['rising']['value'], 'loanQuery' : data1['loan']['rising']['query'], 'loanValue' : data1['loan']['rising']['value']}
    return render(request, 'medical.html', context)



