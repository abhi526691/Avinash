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
    # try:
    all_keywordsFinance = ['finance2025']
    trendshow.build_payload(all_keywordsFinance, cat=0, timeframe='today 1-m', geo='US')
    data1 = trendshow.related_queries()
    if data['insurance']['rising']['query'] is None:
        if data1['finance2025']['rising'] is None:
            return render(request, 'index.html', context={'li':[], 'value':[], 'financeQuery':[], 'financeValue':[]})
        else:
            return render(request, 'index.html', context={'li':[], 'value':[], 'financeQuery' : data1['finance2025']['rising']['query'], 'financeValue' : data1['finance2025']['rising']['value']})
    else:
        if data1['finance2025']['rising'] is None:
            return render(request, 'index.html', {'li' : data['insurance']['rising']['query'], 'value' : data['insurance']['rising']['value'], 'financeQuery':[], 'financeValue':[]})
        else:
            context = {'li' : data['insurance']['rising']['query'], 'value' : data['insurance']['rising']['value'], 'financeQuery' : data1['finance2025']['rising']['query'], 'financeValue' : data1['finance2025']['rising']['value'] }
            return render(request, 'index.html', context)



def medical(request):
    all_keywords = ['medical']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data = trendshow.related_queries()

    all_keywords = ['loan']
    trendshow.build_payload(all_keywords, cat=0, timeframe='today 1-m', geo='US')
    data1 = trendshow.related_queries()

    if data['medical']['rising']['query'] is None:
        if data1['loan']['rising'] is None:
            return render(request, 'medical.html', context={'li':[], 'value':[], 'loanQuery':[], 'loanValue':[]})
        else:
            return render(request, 'medical.html', context={'li':[], 'value':[], 'loanQuery' : data1['loan']['rising']['query'], 'loanValue' : data1['loan']['rising']['value']})
    else:
        if data1['loan']['rising'] is None:
            return render(request, 'medical.html', {'li' : data['medical']['rising']['query'], 'value' : data['medical']['rising']['value'], 'loanQuery':[], 'loanValue':[]})
        else:
            context = {'li' : data['medical']['rising']['query'], 'value' : data['medical']['rising']['value'], 'loanQuery' : data1['loan']['rising']['query'], 'loanValue' : data1['loan']['rising']['value'] }
            return render(request, 'medical.html', context)




