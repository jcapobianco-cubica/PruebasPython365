import Mail
import Sharepoint
import Intune
import User
import asyncio

#print(asyncio.run(Sharepoint.get_siteLists('9a79cede-9388-4705-8425-58ef08aa20b9')))
#print(asyncio.run(Sharepoint.get_listItems('9a79cede-9388-4705-8425-58ef08aa20b9','2b0b1afa-5e92-4ebd-89f1-f5bb83e74fe8')))
#asyncio.run(Mail.main())

#asyncio.run(Intune.get_devices())

#print(asyncio.run(Intune.get_devices()))
#Intune.patch_device
asyncio.run(Intune.patch_device())