import os.path
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import redirect
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from core.views import UserService
from users.services import Credentials
from users.services import CredentialsService
from webapp.secrets import get_secret

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponseBadRequest
from googleapiclient.discovery import build as google_build

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#new-imports
from google_auth_oauthlib.flow import Flow
from google.auth.transport import Request

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",   
]

REDIRECT_URL = f"{settings.BASE_URL}/calendar/redirect/"
API_SERVICE_NAME = "calendar"
API_VERSION = "v3"

@api_view(['GET'])
def calendar_init_view(request):
    config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
    creds = CredentialsService.init_for(request.user, scopes=SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(config, SCOPES)
            flow.redirect_uri = REDIRECT_URL

            authorization_url, state = flow.authorization_url(
                access_type="offline",
                prompt="consent", include_granted_scopes="true"
            )
            request.session["state"] = state

            return JsonResponse({"authorization_url": authorization_url})

    return JsonResponse({"message": "Sucess"})


@api_view(["POST"])
def calendar_token(request):
    config = get_secret(f"{settings.ENVIRONMENT}/google/calendar")
    flow = Flow.from_client_config(config, scopes=SCOPES, redirect_uri="http://localhost:3000")
    code = request.data["code"]
    print("code", code)
    # flow.fetch_token(code)
    # 4/0AdLIrYdjDBOqa7mxm9bGUUdXo_lyOu1YgKIiDh6_UhBCmfZNI_JMkRDLvg33YTHPSaWe2A
    try:
        credentials = flow.fetch_token(code=code)
        print("crendentials:", credentials)
        credentials = Credentials.from_flow(flow.credentials)
        user_service = UserService.from_credentials(credentials)
        user, _ = user_service.update_local(user_service.remote())
        user_service.check_calendar(user)

        login(request, user)
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"sucess": True})