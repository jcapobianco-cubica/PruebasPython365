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
from msgraph.generated.users.item.user_item_request_builder import UserItemRequestBuilder
import time

# Get token
credential = ClientSecretCredential(
    client_secret = secrets.get('CLIENT_SECRET'),
    client_id = secrets.get('CLIENT_ID'),
    tenant_id =  secrets.get('TENANT_ID')
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credentials=credential, scopes=scopes)

def create_mail(from_email,body, subject, recipients, cc_recipient, bcc_recipient):

    # Sender
    sender = EmailAddress()
    sender.address = from_email
    from_recipient = Recipient()
    from_recipient.email_address = sender

    varrecipients = []
    for recipient in recipients:
        # Add recipient per recipient
        recipient_email = EmailAddress()
        recipient_email.address = recipient
        to_recipient = Recipient()
        to_recipient.email_address = recipient_email
        varrecipients.append(to_recipient)

    # CC
    if cc_recipient != []:
        cc_recipients = []
        for cc_ontvanger in cc_recipient:
            # Add cc_recipient per recipient
            cc_recipient_email = EmailAddress()
            cc_recipient_email.address = cc_ontvanger
            cc_recipient = Recipient()
            cc_recipient.email_address = cc_recipient_email
            cc_recipients.append(cc_recipient)

    # BCC
    if bcc_recipient != []:
        bcc_recipients = []
        for bcc_ontvanger in bcc_recipient:
            # Add bcc_recipient per recipient
            bcc_recipient_email = EmailAddress()
            bcc_recipient_email.address = bcc_ontvanger
            bcc_recipient = Recipient()
            bcc_recipient.email_address = bcc_recipient_email
            bcc_recipients.append(bcc_recipient)

    # Message body
    email_body = ItemBody()
    email_body.content = body
    email_body.content_type = BodyType.Html

    # Message object
    message = Message()
    message.subject = subject
    message.from_ = from_recipient
    message.to_recipients = varrecipients

    if cc_recipient != []:
        message.cc_recipients = cc_recipients

    if bcc_recipient != []:
        message.bcc_recipients = bcc_recipients

    message.body = email_body

    # Request object
    request_body = SendMailPostRequestBody()
    request_body.message = message

    return request_body

async def send_mail(mail,sender):
    try:
        await client.users.by_user_id(sender).send_mail.post(mail)
        #workaround 429 throttling error
        #time.sleep(1)
    # Print or handle the response here
    except Exception as e:
        print(e)

async def main():
    sender = "jcapobianco@q7vf.onmicrosoft.com"
    recipient = ["jcapobianco@q7vf.onmicrosoft.com"]
    cc = []
    bcc = []
    subject="Test Email Subject"
    html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Smiley Face</title>
        </head>
        <body>
            <div style="font-size: 48px; text-align: center;">%s</div> 
        </body>
        </html>
        """.replace("\n", "") %"texto"
    
    mailbericht = create_mail(sender, html, subject, recipient, cc, bcc)

    await send_mail(mailbericht,sender)
    # Create a list of tasks to run concurrently
    #tasks = [Mail.send_mail(mailbericht,sender) for _ in range(1, 3)]

    #await asyncio.gather(*tasks)