import asyncio
from Secret import secrets
import requests
from kiota_abstractions.api_error import APIError
import msal
import Authentication

access_token=Authentication.get_token()

async def get_users():    
    graph_results=[]
    url= 'https://graph.microsoft.com/v1.0/users'
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

async def get_assignedLicences():
    graph_results=[]
    filter='$filter=assignedLicenses/$count ne 0'
    count='$count=true'
    select='$select=displayName,createdDateTime,accountEnabled,userPrincipalName,givenName,surname,externalUserState,assignedLicenses,officeLocation'
    url= 'https://graph.microsoft.com/v1.0/users?{}&{}&{}'.format(filter,count,select)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json',
        'ConsistencyLevel': 'eventual'
    }
    while url:
        try:
            graph_result = requests.get(url=url, headers=headers).json()
            graph_results.extend(graph_result['value'])
            url = graph_result['@odata.nextLink']        
        except:
            break
    return graph_results

