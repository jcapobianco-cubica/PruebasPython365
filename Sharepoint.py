import asyncio
import json
from Secret import secrets
import requests
from kiota_abstractions.api_error import APIError
import msal

# Get token
client_secret = secrets.get('CLIENT_SECRET')
client_id = secrets.get('CLIENT_ID')
tenant_id =  secrets.get('TENANT_ID')
authority= 'https://login.microsoftonline.com/{}'.format(secrets.get('TENANT_ID'))
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

async def get_sites():
    graph_results=[]
    url= 'https://graph.microsoft.com/v1.0/sites/getAllSites'
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    while url:
        try:
            graph_result = requests.get(url=url, headers=headers).json()
            graph_results.extend(graph_result['value'])
            url = graph_result['@odata.nextLink']        
        except:
            break
    return graph_results

async def get_countsites():
    graph_results=[]
    url= 'https://graph.microsoft.com/v1.0/sites/getAllSites'
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    while url:
        try:
            graph_result =  requests.get(url=url, headers=headers).json()
            graph_results.extend(graph_result['value'])
            url = graph_result['@odata.nextLink']        
        except:
            break
    return len(graph_results)

async def get_siteLists(site):
    graph_results=[]
    url= 'https://graph.microsoft.com/v1.0/sites/{}/lists'.format(site)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    while url:
        try:
            graph_result = requests.get(url=url, headers=headers).json()
            graph_results.extend(graph_result['value'])
            url = graph_result['@odata.nextLink']        
        except:
            break
    return graph_results

async def get_listItems(site,list):
    graph_results=[]
    listExport=[]
    
    url= 'https://graph.microsoft.com/v1.0/sites/{}/lists/{}/items?expand=fields'.format(site,list)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }    
    while url:
        try:
            graph_result = requests.get(url=url, headers=headers).json()
            graph_results.extend(graph_result['value'])
            url = graph_result['@odata.nextLink']                   
        except:
            break

    
    for x in graph_results:
        jsonExport={}        
        for y in x['fields']:
            jsonExport[y]=x['fields'][y]            
        listExport.append(jsonExport)

    return listExport
    #return json.dumps(listExport)