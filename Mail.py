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

from_email="automatisering@contoso.com"

# HTML content with a smiley
html = ""

def mail_body():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smiley Face</title>
    </head>
    <body>
        <div style="font-size: 48px; text-align: center;">&#128512;</div>
    </body>
    </html>
    """.replace("\n", "")

def create_mail(bericht_html: str, titel, ontvangers: list, cc_ontvangers: list = [], bcc_ontvangers: list = []):
    '''
    Create a valid mail object to be sent using Microsoft Graph API.

    Parameters:
    - bericht_html (str): The HTML content of the email body.
    - titel (str): The subject of the email.
    - ontvangers (list): A list of recipient email addresses.
    - cc_ontvangers (list, optional): A list of email addresses to be included in the CC field.
    - bcc_ontvangers (list, optional): A list of email addresses to be included in the BCC field.
    - versturende_email (str, optional): The email address of the sender.

    Returns:
    SendMailPostRequestBody: An object representing the mail to be sent.
    '''
    # Sender
    sender = EmailAddress()
    sender.address = from_email
    from_recipient = Recipient()
    from_recipient.email_address = sender

    recipients = []
    for ontvanger in ontvangers:
        # Add recipient per recipient
        recipient_email = EmailAddress()
        recipient_email.address = ontvanger
        to_recipient = Recipient()
        to_recipient.email_address = recipient_email
        recipients.append(to_recipient)

    # CC
    if cc_ontvangers != []:
        cc_recipients = []
        for cc_ontvanger in cc_ontvangers:
            # Add cc_recipient per recipient
            cc_recipient_email = EmailAddress()
            cc_recipient_email.address = cc_ontvanger
            cc_recipient = Recipient()
            cc_recipient.email_address = cc_recipient_email
            cc_recipients.append(cc_recipient)

    # BCC
    if bcc_ontvangers != []:
        bcc_recipients = []
        for bcc_ontvanger in bcc_ontvangers:
            # Add bcc_recipient per recipient
            bcc_recipient_email = EmailAddress()
            bcc_recipient_email.address = bcc_ontvanger
            bcc_recipient = Recipient()
            bcc_recipient.email_address = bcc_recipient_email
            bcc_recipients.append(bcc_recipient)

    # Message body
    email_body = ItemBody()
    email_body.content = bericht_html
    email_body.content_type = BodyType.Html

    # Message object
    message = Message()
    message.subject = titel
    message.from_escaped = from_recipient
    message.to_recipients = recipients

    if cc_ontvangers != []:
        message.cc_recipients = cc_recipients

    if bcc_ontvangers != []:
        message.bcc_recipients = bcc_recipients

    message.body = email_body

    # Request object
    request_body = SendMailPostRequestBody()
    request_body.message = message

    return request_body

async def send_mail(mailbericht):
    try:
        response = await client.users.by_user_id(from_email).send_mail.post(mailbericht)
        #workaround 429 throttling error
        time.sleep(1)
    # Print or handle the response here
    except Exception as e:
        print(e)
