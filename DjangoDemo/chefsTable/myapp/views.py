from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def Home(request):
    
    return render(request,'home.html')

def drinks(request,coffeeName):
    coffee = [
        {
            'Espresso' :'A strong, concentrated coffee shot with a rich crema on top.'
        },
        {
            'Latte':'A smooth blend of espresso and steamed milk with a light foam.'
        },
        {
            'Cappucino':'A bold espresso topped with equal parts steamed milk and frothy foam.'
        },
    ]
    printCoffe = list(coffee[0].keys())[0]
    coffeeName = printCoffe
    content = f"<html><body><h1>Welcome Boss </br>{printCoffe}</br>{coffee[0][printCoffe]}</h1></body></html>"
    return HttpResponse(content)