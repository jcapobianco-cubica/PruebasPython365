import secrets
import Mail
import Sharepoint
import asyncio

#asyncio.run(Sharepoint.get_users())

async def main():
    recipient = ["jcapobianco@q7vf.onmicrosoft.com"]
    cc = []
    bcc = []

    mailbericht = Mail.create_mail(Mail.html, "Test Email Subject", recipient, cc, bcc)

    # Create a list of tasks to run concurrently
    tasks = [Mail.send_mail(mailbericht) for _ in range(1, 5)]

    await asyncio.gather(*tasks)


asyncio.run(main())