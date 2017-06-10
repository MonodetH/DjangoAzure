"""
Definition of views.
"""

import httplib, json
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from bs4 import BeautifulSoup

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    # get item
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '99fd5eb582914f7a8595822812988b94',
    }

    body = {"documents": [{"id": "1", "text": "pantalla mala, 16Gb de memoria"}]}

    conn = httplib.HTTPSConnection('api.mercadolibre.com')
    conn.request("GET",
                 "/items/MLC443958984?access_token=APP_USR-3443485718526955-061017-d1f66ff2a267adde4dd51cf57dc7b817__A_K__-4452942",
                 body="{}", headers=headers)
    response = conn.getresponse()
    item = response.read()
    conn.close()

    # description
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '99fd5eb582914f7a8595822812988b94',
    }

    body = {"documents": [{"id": "1", "text": "pantalla mala, 16Gb de memoria"}]}

    conn = httplib.HTTPSConnection('api.mercadolibre.com')
    conn.request("GET",
                 "/items/MLC443958984/description",
                 body="{}", headers=headers)
    response = conn.getresponse()
    desc = BeautifulSoup(json.loads(response.read().decode("utf-8"))["text"]).get_text()
    conn.close()

    print(desc)
    print(type(desc))

    # sentiment
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '99fd5eb582914f7a8595822812988b94',
    }

    query = {"documents": [{"id": "1", "text": desc}]}

    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases", body=json.dumps(query), headers=headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()

    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'sentiment':data,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )