"""
Definition of views.
"""

import httplib, urllib, base64
import urllib2
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '99fd5eb582914f7a8595822812988b94',
    }

    params = urllib.urlencode({
    })

    body = {"documents":[{"id":"1", "text":"pantalla mala, 16Gb de memoria"}]}


    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases" % params, "{body}", headers)
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
            #'sentiment':data,
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
