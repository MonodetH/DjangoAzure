"""
Definition of views.
"""

import httplib
import urllib
import base64
import json
#import requests
import urllib2
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import sys
from lib import meli

sys.path.append('../lib')
#from meli import Meli

LISTAPROD = []


#Metodo para obtener el ID de un item mediante su url
def getItemId(url):

	palabra = url.split("-")
	idProducto = palabra[0][-3:] + palabra[1]

	return idProducto


#Getters necesarios para la utilizacion de la API de Mercado Libre
def getAccesToken():
	return "APP_USR-3443485718526955-061012-5040dcc4526436d12d4332900dcbca32__I_F__-4452942"

def getAppId():
	return "3443485718526955"

def getSecretKey():
	return "nozaVGHtkmuR6sYdOmlTq8WYkMPvqw08"

def getRefreshToken():
	return ""

#Metodo para poder obtener las caracteristicas del producto y pasarselas a un objeto
def getItem(itemid):
    consulta = meli.Meli(client_id=getAppId(), client_secret=getSecretKey(), access_token=getAccesToken(),refresh_token = "")

    respuesta = consulta.get("/item/" + itemid)

    producto = json.loads(respuesta.content)

    return producto

#Metodo para agregar productos a una lista de productos
def addProductsList(urlProducto):

    producto = getItem(getItemId(urlProducto))

    global LISTAPROD

    LISTAPROD.append(producto)




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    # headers = {
    #     # Request headers
    #     'Content-Type': 'application/json',
    #     'Ocp-Apim-Subscription-Key': '99fd5eb582914f7a8595822812988b94',
    # }
    #
    # params = urllib.urlencode({
    # })
    #
    # body = {"documents":[{"id":"1", "text":"pantalla mala, 16Gb de memoria"}]}
    #
    #
    # conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    # conn.request("POST", "/text/analytics/v2.0/keyPhrases" % params, json.dumps(body), headers)
    # response = conn.getresponse()
    # data = response.read()
    # print(data)
    # conn.close()

    #r = requests.post("https://westus.api.cognitive.microsoft.com", data={"documents":[{"id":"1", "text":"pantalla mala, 16Gb de memoria"}]'})

    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'listaProductos':LISTAPROD,
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



