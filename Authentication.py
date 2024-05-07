import asyncio
from Secret import secrets
import requests
from kiota_abstractions.api_error import APIError
import msal

def get_token():
    # Get token
    client_secret = secrets.get('CLIENT_SECRET')
    client_id = secrets.get('CLIENT_ID')
    tenant_id =  secrets.get('TENANT_ID')
    authority= 'https://login.microsoftonline.com/{}'.format(tenant_id)
    scope = ['https://graph.microsoft.com/.default']

    # Create an MSAL instance providing the client_id, authority and client_credential parameters
    client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

    # First, try to lookup an access token in cache
    token_result = client.acquire_token_silent(scope, account=None)
    access_token=''

    # If the token is available in cache, save it to a variable
    if token_result:
        access_token = 'Bearer ' + token_result['access_token']

    # If the token is not available in cache, acquire a new one from Azure AD and save it to a variable
    if not token_result:
        token_result = client.acquire_token_for_client(scopes=scope)
        access_token = 'Bearer ' + token_result['access_token']
    
    return access_token
