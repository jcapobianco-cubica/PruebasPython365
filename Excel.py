import asyncio
from Secret import secrets
import requests
from kiota_abstractions.api_error import APIError
import msal
import Authentication
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()




