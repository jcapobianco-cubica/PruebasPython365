import asyncio
import json
from Secret import secrets
import requests
from kiota_abstractions.api_error import APIError
import msal
import Authentication

access_token=Authentication.get_token()
headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }

def get_searchSite(siteName):
    url='https://graph.microsoft.com/v1.0/sites?search={}'.format(siteName)    
    graph_result = requests.get(url=url, headers=headers).json()
    return graph_result['value'][0]['id'].split(",")[1]

def get_searchList(siteName,listName):
    siteId=get_searchSite(siteName)
    url='https://graph.microsoft.com/v1.0/sites/{}/lists/{}'.format(siteId,listName)
    graph_result = requests.get(url=url, headers=headers).json()
    return graph_result['id']

def get_listItems(siteName,listName):
    graph_results=[]
    listExport=[]
    siteId=get_searchSite(siteName)
    listId=get_searchList(siteName,listName)
    url= 'https://graph.microsoft.com/v1.0/sites/{}/lists/{}/items?expand=fields'.format(siteId,listId)
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

    return json.dumps(listExport)
        
async def del_emptyList(siteName, listName):
    url= 'https://graph.microsoft.com/v1.0/sites/{}/lists/{}/items?expand=fields'.format(site,list)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }  

async def get_drives(siteName):
    url= 'https://graph.microsoft.com/v1.0/sites/{}/lists/{}/items?expand=fields'.format(siteName,list)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }  

async def post_createFile(siteId,folder,fileName):
    url= 'https://graph.microsoft.com/v1.0/sites/{}/drive/items/{}:/{}:/content'.format(siteId,folder,fileName)

async def get_permissions():
    url=''

print(get_listItems('MSFT','Usuarios activos'))