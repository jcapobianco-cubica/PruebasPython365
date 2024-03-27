import secrets
import Mail
import Sharepoint
import asyncio
import Intune

#asyncio.run(Sharepoint.get_users())

#asyncio.run(Mail.main())

#asyncio.run(Intune.get_devices())

print(asyncio.run(Intune.get_devices()))