import asyncio
from Secrets import secrets
from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.item.send_mail.send_mail_post_request_body import SendMailPostRequestBody
from msgraph.generated.models.body_type import BodyType
from msgraph.generated.models.message import Message
from msgraph.generated.models.email_address import EmailAddress
from msgraph.generated.models.importance import Importance
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.recipient import Recipient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder
import time

# Get token
credential = ClientSecretCredential(
    client_secret = secrets.get('CLIENT_SECRET'),
    client_id = secrets.get('CLIENT_ID'),
    tenant_id =  secrets.get('TENANT_ID')
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credentials=credential, scopes=scopes)

async def test(sender):
    print(await client.users.by_user_id(sender).send_mail)

s = "jcapobianco@q7vf.onmicrosoft.com"
asyncio.run(test(s))