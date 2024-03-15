from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.lists.list import List
from Secrets import secrets

# Parametros de SharePoint
site_url = 'https://q7vf.sharepoint.com/sites/MSFT'
secret_key = secrets.get('SECRET_KEY')
client_id = secrets.get('CLIENT_ID')
ctx = ''

def createToken():
    ctx_auth = AuthenticationContext(site_url)
    if ctx_auth.acquire_token_for_app(client_id,secret_key):
        ctx = ClientContext(site_url,ctx_auth)
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()
    
def createFolder():
    root_folder = ctx.web.default_document_library().root_folder
    folder = root_folder.folders.add(
        "archive", color_hex=FolderColors.DarkGreen
    ).execute_query()
