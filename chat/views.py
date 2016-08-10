
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404, QueryDict


import os
import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.template.loader import render_to_string
from django.utils import timezone

from faker import Factory
from twilio.access_token import AccessToken, IpMessagingGrant

from django.contrib.auth.decorators import login_required

def test(request):
    if request.method=='GET':
        return JsonResponse({"message":"OK"})
      
def main(request):
    if request.method=='GET':
        return render(request,'chat.html',{})
      
@login_required
def token(request):
    fake = Factory.create()
    # get credentials for environment variables
#    account_sid = os.environ['TWILIO_ACCOUNT_SID']
#    api_key = os.environ['TWILIO_API_KEY']
#    api_secret = os.environ['TWILIO_API_SECRET']
#    service_sid = os.environ['TWILIO_IPM_SERVICE_SID']
    
    account_sid = "ACc8d160e25f25dcd5031b180821428fc0"
    api_key = "SK05b65992fd32b9b92e6bdb1cd1ea5380"
    api_secret = "sBsSZAIuGeBtntI8kkly3h6mJk5KfM7S"
    service_sid = "ISfd35cbde546d43559e194bb240a1e95c"
    
#    export TWILIO_ACCOUNT_SID="ACc8d160e25f25dcd5031b180821428fc0"
#    export TWILIO_API_KEY="SK05b65992fd32b9b92e6bdb1cd1ea5380"
#    export TWILIO_API_SECRET="sBsSZAIuGeBtntI8kkly3h6mJk5KfM7S"
#    export TWILIO_IPM_SERVICE_SID="ISfd35cbde546d43559e194bb240a1e95c"
    
    # create a randomly generated username for the client
    identity = fake.user_name()

    # Create a unique endpoint ID for the 
    device_id = 'broswer'
    endpoint = "TwilioChatDemo:{0}:{1}".format(identity, device_id)

    # Create access token with credentials
    token = AccessToken(account_sid, api_key, api_secret, identity)

    # Create an IP Messaging grant and add to token
    ipm_grant = IpMessagingGrant(endpoint_id=endpoint, service_sid=service_sid)
    token.add_grant(ipm_grant)
    
    # Return token info as JSON
    return JsonResponse({"identity":identity, "token":token.to_jwt()})