import asyncio
from Secrets import secrets
from msgraph import GraphServiceClient
from azure.identity import ClientSecretCredential

# Parametros de SharePoint
credential = ClientSecretCredential(
    client_secret = secrets.get('CLIENT_SECRET'),
    client_id = secrets.get('CLIENT_ID'),
    tenant_id =  secrets.get('TENANT_ID')
)
scopes = ['https://graph.microsoft.com/.default']

client = GraphServiceClient(credentials=credential, scopes=scopes)

async def get_users():
    users = await client.users.get()
    if users and users.value:
        for user in users.value:
            print(user.id, user.user_principal_name)
asyncio.run(get_users())