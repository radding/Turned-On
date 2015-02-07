"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest JsonRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
   return JsonRequest({"text":"hi"})

def sendSmsVerificationCode(request):
	from twilio.rest import TwilioRestClient

	fromNumber = "+14012065509"
	ACCOUNT_SID = "ACf3f0805e01bc0a3db41e7aae79bc96d5"
	AUTH_TOKEN = "acf544c7ffb70d7b888eabc81d75698a"

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	verificationCode = "1234"
	userPhoneNumberToVerify = "2063838296"

	client.messages.create(
		to=userPhoneNumberToVerify,
		from_=fromNumber,
		body="Here is your TurnedOn verification code: " + verificationCode,
	)

	response = HttpResponse()
	response.status_code = 200
	return response

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
