import secrets
import Mail
import Sharepoint
import asyncio

#asyncio.run(Sharepoint.get_users())

async def main():
    sender = "jcapobianco@q7vf.onmicrosoft.com"
    recipient = ["jcapobianco@q7vf.onmicrosoft.com"]
    cc = []
    bcc = []
    subject="Test Email Subject"

    mailbericht = Mail.create_mail(sender, Mail.html, subject, recipient, cc, bcc)

    await Mail.send_mail(mailbericht,sender)
    # Create a list of tasks to run concurrently
    #tasks = [Mail.send_mail(mailbericht,sender) for _ in range(1, 3)]

    #await asyncio.gather(*tasks)


asyncio.run(main())