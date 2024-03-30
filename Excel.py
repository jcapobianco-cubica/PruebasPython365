import asyncio
from Secret import secrets
import requests
from kiota_abstractions.api_error import APIError
import msal
import Authentication
import xlsxwriter
import os.path

def post_createFile():
    #workbook=''
    #if(os.path.isfile('hello.xlsx')==False):
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.add_table('A1:G2', {'name': 'Usuarios',
                                  'columns': [{'header': 'Product'},
                                          {'header': 'Usuario'},
                                          {'header': 'Creado'},
                                          {'header': 'Nombre'},
                                          {'header': 'Apellido'},
                                          {'header': 'Apellido2'},
                                          {'header': 'Apellido3'}
                                          ]})
    workbook.close()

post_createFile()




