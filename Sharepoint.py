import asyncio
from Secret import secrets
from msgraph import GraphServiceClient
from azure.identity import ClientSecretCredential
from kiota_abstractions.api_error import APIError

# Parametros de API
credential = ClientSecretCredential(
    client_secret = secrets.get('CLIENT_SECRET'),
    client_id = secrets.get('CLIENT_ID'),
    tenant_id =  secrets.get('TENANT_ID')
)
scopes = ['https://graph.microsoft.com/.default']

client = GraphServiceClient(credentials=credential, scopes=scopes)

usersArray=[]

async def get_users():
    try:
        users = await client.users.get()
        if users and users.value:
            for user in users.value:
                print(user.id, ",", user.user_principal_name)
                usersArray.append(user.id)
        while users is not None and users.odata_next_link is not None:
            users = await client.users.with_url(users.odata_next_link).get()
            if users and users.value:
                for user in users.value:
                    print(user.id, ",", user.user_principal_name)
                    usersArray.append(user.id)
    except APIError as e:
        print (e.error.message)


