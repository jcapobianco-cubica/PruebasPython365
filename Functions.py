import asyncio
import Authentication
import Sharepoint
import User
from pandas.tseries.offsets import BMonthEnd
from datetime import timedelta,date,datetime
import json

def get_licences():
    licences="""[
    {
        "GUID": "e4654015-5daf-4a48-9b37-4f309dddd88b",
        "Titulo": "Advanced Communications"
    },
    {
        "GUID": "d2dea78b-507c-4e56-b400-39447f4738f8",
        "Titulo": "Complemento de capacidad de AI Builder"
    },
    {
        "GUID": "8f0c5670-4e56-4892-b06d-91c085d7004f",
        "Titulo": "App Connect de IW"
    },
    {
        "GUID": "9706eed9-966f-4f1b-94f6-bb2b4af99a5b",
        "Titulo": "Complemento de gobernanza de aplicaciones para Miicrosoft Defender for Cloud Apps"
    },
    {
        "GUID": "0c266dff-15dd-4b49-8397-2bb16070ed52",
        "Titulo": "Audioconferencia de Microsoft 365"
    },
    {
        "GUID": "2b9c8e7c-319c-43a2-a2a0-48c5c6161de7",
        "Titulo": "Azure Active Directory Basic"
    },
    {
        "GUID": "078d2b04-f1bd-4111-bbd4-b4b1b354cef4",
        "Titulo": "Azure Active Directory Premium P1"
    },
    {
        "GUID": "30fc3c36-5a95-4956-ba57-c09c2a600bb9",
        "Titulo": "Azure Active Directory Premium P1 o P2 para profesores"
    },
    {
        "GUID": "84a661c4-e949-4bd2-a560-ed7766fcaf2b",
        "Titulo": "Azure Active Directory Premium P2"
    },
    {
        "GUID": "c52ea49f-fe5d-4e95-93ba-1de91d380f89",
        "Titulo": "Azure Information Protection (Plan 1)"
    },
    {
        "GUID": "78362de1-6942-4bb8-83a1-a32aa67e6e2c",
        "Titulo": "Azure Information Protection Premium P1 para Government"
    },
    {
        "GUID": "90d8b3f8-712e-4f7b-aa1e-62e7ae6cbe96",
        "Titulo": "Aplicaciones empresariales (gratis)"
    },
    {
        "GUID": "631d5fb1-a668-4c2a-9427-8830665a742e",
        "Titulo": "Common Data Service para la capacidad de archivos de aplicaciones"
    },
    {
        "GUID": "e612d426-6bc3-4181-9658-91aa906b0ac0",
        "Titulo": "Capacidad de la base de datos de Common Data Service"
    },
    {
        "GUID": "eddf428b-da0e-4115-accf-b29eb0b83965",
        "Titulo": "Capacidad de bases de datos de Common Data Service para la administración pública"
    },
    {
        "GUID": "448b063f-9cc6-42fc-a0e6-40e08724a395",
        "Titulo": "Capacidad de registro de Common Data Service"
    },
    {
        "GUID": "47794cd0-f0e5-45c5-9033-2eb6b5fc84e0",
        "Titulo": "Créditos de comunicaciones"
    },
    {
        "GUID": "8a5fbbed-8b8c-41e5-907e-c50c471340fd",
        "Titulo": "Complemento de evaluación prémium del Administrador de cumplimiento"
    },
    {
        "GUID": "a9d7ef53-9bea-4a2a-9650-fa7df58fe094",
        "Titulo": "Complemento de evaluación prémium del Administrador de cumplimiento para GCC"
    },
    {
        "GUID": "a9c51c15-ffad-4c66-88c0-8771455c832d",
        "Titulo": "Inteligencia sobre amenazas de Defender"
    },
    {
        "GUID": "328dc228-00bc-48c6-8b09-1fbc8bc3435d",
        "Titulo": "Dynamics 365: almacenamiento de base de datos adicional (oferta calificada)"
    },
    {
        "GUID": "9d776713-14cb-4697-a21d-9a52455c738a",
        "Titulo": "Dynamics 365: instancia de producción adicional (oferta calificada)"
    },
    {
        "GUID": "e06abcc2-7ec5-4a79-b08b-d9c282376f72",
        "Titulo": "Dynamics 365: instancia de no producción adicional (oferta calificada)"
    },
    {
        "GUID": "c6df1e30-1c9f-427f-907c-3d913474a1c7",
        "Titulo": "Dynamics 365 AI for Market Insights (versión preliminar)"
    },
    {
        "GUID": "673afb9d-d85b-40c2-914e-7bf46cd5cd75",
        "Titulo": "Recursos adicionales de administración de recursos de Dynamics 365"
    },
    {
        "GUID": "a58f5506-b382-44d4-bfab-225b2fbf8390",
        "Titulo": "Complemento de entorno adicional de Dynamics 365 Business Central"
    },
    {
        "GUID": "7d0d4f9a-2686-4cb8-814c-eff3fdab6d74",
        "Titulo": "Capacidad de base de datos de Dynamics 365 Business Central"
    },
    {
        "GUID": "2880026b-2b0c-4251-8656-5d41ff11e3aa",
        "Titulo": "Dynamics 365 Business Central Essentials"
    },
    {
        "GUID": "9a1e33ed-9697-43f3-b84c-1b0959dbb1d4",
        "Titulo": "Contable externo de Dynamics 365 Business Central"
    },
    {
        "GUID": "6a4a1628-9b9a-424d-bed5-4118f0ede3fd",
        "Titulo": "Dynamics 365 Business Central para IW"
    },
    {
        "GUID": "f991cecc-3f91-4cd0-a9a8-bf1c8167e029",
        "Titulo": "Dynamics 365 Business Central Premium"
    },
    {
        "GUID": "2e3c4023-80f6-4711-aa5d-29e0ecb46835",
        "Titulo": "Dynamics 365 Business Central Team Members"
    },
    {
        "GUID": "1508ad2d-5802-44e6-bfe8-6fb65de63d28",
        "Titulo": "Prueba de Dynamics 365 Commerce"
    },
    {
        "GUID": "ea126fc5-a19e-42e2-a731-da9d437bffcf",
        "Titulo": "Plan Dynamics 365 Customer Engagement Plan"
    },
    {
        "GUID": "a3d0cd86-8068-4071-ad40-4dc5b5908c4b",
        "Titulo": "Anexación de Dynamics 365 Customer Insights"
    },
    {
        "GUID": "036c2481-aa8a-47cd-ab43-324f0c157c2d",
        "Titulo": "Dynamics 365 Customer Insights vTrial"
    },
    {
        "GUID": "1e615a51-59db-4807-9957-aa83c3657351",
        "Titulo": "Dynamics 365 Customer Service Enterprise Viral Evaluación"
    },
    {
        "GUID": "eb18b715-ea9d-4290-9994-2ebf4b5042d2",
        "Titulo": "Agregación de Dynamics 365 for Customer Service Enterprise a la oferta base calificada de Dynamics 365 A"
    },
    {
        "GUID": "61e6bd70-fbdb-4deb-82ea-912842f39431",
        "Titulo": "Prueba de Dynamics 365 Customer Service Insights"
    },
    {
        "GUID": "bc946dac-7877-4271-b2f7-99d2db13cd2c",
        "Titulo": "Prueba de Dynamics 365 Customer Voice"
    },
    {
        "GUID": "1439b6e2-5d59-4873-8c59-d60e2a196e92",
        "Titulo": "Dynamics 365 Customer Service Professional"
    },
    {
        "GUID": "359ea3e6-8130-4a57-9f8f-ad897a0342f1",
        "Titulo": "Dynamics 365 Customer Voice"
    },
    {
        "GUID": "446a86f8-a0cb-4095-83b3-d100eb050e3d",
        "Titulo": "Respuestas adicionales de Dynamics 365 Customer Voice"
    },
    {
        "GUID": "65f71586-ade3-4ce1-afc0-1b452eaf3782",
        "Titulo": "Respuestas adicionales de Dynamics 365 Customer Voice"
    },
    {
        "GUID": "e2ae107b-a571-426f-9367-6d4c8f1390ba",
        "Titulo": "USL de Dynamics 365 Customer Voice"
    },
    {
        "GUID": "a4bfb28e-becc-41b0-a454-ac680dc258d3",
        "Titulo": "Dynamics 365 Enterprise Edition: portal adicional (oferta calificada)"
    },
    {
        "GUID": "29fcd665-d8d1-4f34-8eed-3811e3fca7b3",
        "Titulo": "Dynamics 365 Field Service Viral Trial"
    },
    {
        "GUID": "55c9eb4e-c746-45b4-b255-9ab6b19d5c62",
        "Titulo": "Dynamics 365 Finance"
    },
    {
        "GUID": "d39fb075-21ae-42d0-af80-22a2599749e0",
        "Titulo": "Dynamics 365 for Case Management Enterprise Edition"
    },
    {
        "GUID": "94a6fbd4-6a2f-4990-b356-dc7dd8bed08a",
        "Titulo": "Administrador de organización de Dynamics 365 Customer Service"
    },
    {
        "GUID": "749742bf-0d37-4158-a120-33567104deeb",
        "Titulo": "Dynamics 365 for Customer Service Enterprise Edition"
    },
    {
        "GUID": "7d7af6c2-0be6-46df-84d1-c181b0272909",
        "Titulo": "Chat de Dynamics 365 for Customer Service"
    },
    {
        "GUID": "a36cdaa2-a806-4b6e-9ae0-28dbd993c20e",
        "Titulo": "Agregación de Dynamics 365 for Field Service a la oferta base calificada de Dynamics 365"
    },
    {
        "GUID": "c7d15985-e746-4f01-b113-20b575898250",
        "Titulo": "Dynamics 365 for Field Service Enterprise Edition"
    },
    {
        "GUID": "977464c4-bfaf-4b67-b761-a9bb735a2196",
        "Titulo": "Dynamics 365 Field Service, Enterprise Edition: optimización de programación de recursos"
    },
    {
        "GUID": "cc13a803-544e-4464-b4e4-6d6169a138fa",
        "Titulo": "Dynamics 365 for Financials Business Edition"
    },
    {
        "GUID": "de176c31-616d-4eae-829a-718918d7ec23",
        "Titulo": "Conector híbrido de Dynamics 365"
    },
    {
        "GUID": "99c5688b-6c75-4496-876f-07f0fbd69add",
        "Titulo": "Aplicación adicional de Dynamics 365 for Marketing"
    },
    {
        "GUID": "23053933-0fda-431f-9a5b-a00fd78444c1",
        "Titulo": "Contactos adicionales de Nivel 3 de Dynamics 365 for Marketing"
    },
    {
        "GUID": "c393e9bd-2335-4b46-8b88-9e2a86a85ec1",
        "Titulo": "Aplicación adicional que no es de producción de Dynamics 365 for Marketing"
    },
    {
        "GUID": "d8eec316-778c-4f14-a7d1-a0aca433b4e7",
        "Titulo": "Contactos adicionales de Nivel 5 de Dynamics 365 for Marketing"
    },
    {
        "GUID": "85430fb9-02e8-48be-9d7e-328beb41fa29",
        "Titulo": "Agregación Dynamics 365 for Marketing"
    },
    {
        "GUID": "238e2f8d-e429-4035-94db-6926be4ffe7b",
        "Titulo": "Dynamics 365 for Marketing Business Edition"
    },
    {
        "GUID": "4b32a493-9a67-4649-8eb9-9fc5a5f75c12",
        "Titulo": "USL de Dynamics 365 for Marketing"
    },
    {
        "GUID": "8edc2cf8-6438-4fa9-b6e3-aa1660c640cc",
        "Titulo": "Dynamics 365 for Sales and Customer Service Enterprise Edition"
    },
    {
        "GUID": "1e1a282c-9c54-43a2-9310-98ef728faace",
        "Titulo": "Dynamics 365 for Sales Enterprise Edition"
    },
    {
        "GUID": "2edaa1dc-966d-4475-93d6-8ee8dfd96877",
        "Titulo": "Dynamics 365 Sales Premium"
    },
    {
        "GUID": "be9f9771-1c64-4618-9907-244325141096",
        "Titulo": "Dynamics 365 for Sales Professional"
    },
    {
        "GUID": "9c7bff7a-3715-4da7-88d3-07f57f8d0fb6",
        "Titulo": "Dynamics 365 for Sales Professional Trial"
    },
    {
        "GUID": "245e6bf9-411e-481e-8611-5c08595e2988",
        "Titulo": "Adjuntar Dynamics 365 for Sales Professional a la oferta base calificada de Dynamics 365"
    },
    {
        "GUID": "f2e48cb3-9da0-42cd-8464-4a54ce198ad0",
        "Titulo": "Dynamics 365 for Supply Chain Management"
    },
    {
        "GUID": "3a256e9a-15b6-4092-b0dc-82993f4debc6",
        "Titulo": "Dynamics 365 for Talent"
    },
    {
        "GUID": "8e7a3d30-d97d-43ab-837c-d7701cef83dc",
        "Titulo": "DYNAMICS 365 for Team Members Enterprise Edition"
    },
    {
        "GUID": "0a389a77-9850-4dc4-b600-bc66fdfefc60",
        "Titulo": "Dynamics 365 Guides"
    },
    {
        "GUID": "3bbd44ed-8a70-4c07-9088-6232ddbd5ddd",
        "Titulo": "Dynamics 365 Operations - Dispositivo"
    },
    {
        "GUID": "e485d696-4c87-4aac-bf4a-91b2fb6f0fa7",
        "Titulo": "Dynamics 365 Operations - Espacio aislado de nivel 2: prueba de aceptación estándar"
    },
    {
        "GUID": "f7ad4bca-7221-452c-bdb6-3e6089f25e06",
        "Titulo": "Dynamics 365 Operations - Espacio aislado de nivel 4: prueba de rendimiento estándar"
    },
    {
        "GUID": "338148b6-1b11-4102-afb9-f92b6cdc0f8d",
        "Titulo": "Dynamics 365 P1 Trial para trabajadores de la información"
    },
    {
        "GUID": "7ed4877c-0863-4f69-9187-245487128d4f",
        "Titulo": "Dynamics 365 Regulatory Service: Enterprise Edition Evaluación"
    },
    {
        "GUID": "7a551360-26c4-4f61-84e6-ef715673e083",
        "Titulo": "Dynamics 365 Remote Assist"
    },
    {
        "GUID": "e48328a2-8e98-4484-a70f-a99f8ac9ec89",
        "Titulo": "Dynamics 365 Remote Assist con HoloLens"
    },
    {
        "GUID": "5b22585d-1b71-4c6b-b6ec-160b1a9c2323",
        "Titulo": "Agregación de Dynamics 365 Sales Enterprise a la oferta base calificada de Dynamics 365"
    },
    {
        "GUID": "6ec92958-3cc1-49db-95bd-bc6b3798df71",
        "Titulo": "Dynamics 365 Sales Premium Viral Evaluación"
    },
    {
        "GUID": "e561871f-74fa-4f02-abee-5b0ef54dd36d",
        "Titulo": "Dynamics 365 Talent: Attract"
    },
    {
        "GUID": "b56e7ccc-d5c7-421f-a23b-5c18bdbad7c0",
        "Titulo": "Dynamics 365 Talent: Onboard"
    },
    {
        "GUID": "7ac9fe77-66b7-4e5e-9e46-10eed1cff547",
        "Titulo": "Dynamics 365 Team Members"
    },
    {
        "GUID": "ccba3cfe-71ef-423a-bd87-b6df3dce59a9",
        "Titulo": "Dynamics 365 UNF OPS Plan ENT Edition"
    },
    {
        "GUID": "aedfac18-56b8-45e3-969b-53edb4ba4952",
        "Titulo": "Enterprise Mobility + Security A3 for Faculty"
    },
    {
        "GUID": "efccb6f7-5641-4e0e-bd10-b4976e1bf68e",
        "Titulo": "Enterprise Mobility + Security E3"
    },
    {
        "GUID": "b05e124f-c7cc-45a0-a6aa-8cf78c946968",
        "Titulo": "Enterprise Mobility + Security E5"
    },
    {
        "GUID": "c793db86-5237-494e-9b11-dcd4877c2c8c",
        "Titulo": "Enterprise Mobility + Security G3 GCC"
    },
    {
        "GUID": "8a180c2b-f4cf-4d44-897c-3d32acc4a60b",
        "Titulo": "Enterprise Mobility + Security G5 GCC"
    },
    {
        "GUID": "e8ecdf70-47a8-4d39-9d15-093624b7f640",
        "Titulo": "Servicios de Exchange Enterprise CAL (EOP, DLP)"
    },
    {
        "GUID": "4b9405b0-7788-4568-add1-99614e613b69",
        "Titulo": "Exchange Online (plan 1)"
    },
    {
        "GUID": "ad2fe44a-915d-4e2b-ade1-6766d50a9d9c",
        "Titulo": "Exchange Online (plan 1) para alumnos"
    },
    {
        "GUID": "aa0f9eb7-eff2-4943-8424-226fb137fcad",
        "Titulo": "Exchange Online (plan 1) para ex alumnos con Yammer"
    },
    {
        "GUID": "19ec0d23-8335-4cbd-94ac-6050e30712fa",
        "Titulo": "Exchange Online (PLAN 2)"
    },
    {
        "GUID": "0b7b15a8-7fd2-4964-bb96-5a566d4e3c15",
        "Titulo": "Exchange Online (Plan 2) para profesores"
    },
    {
        "GUID": "7be8dc28-4da4-4e6d-b9b9-c60f2806df8a",
        "Titulo": "Exchange Online (Plan 2) para GCC"
    },
    {
        "GUID": "ee02fd1b-340e-4a4b-b355-4a514e4c8943",
        "Titulo": "Archivado de Exchange Online for Exchange Online"
    },
    {
        "GUID": "90b5e015-709a-4b8b-b08e-3200f994494c",
        "Titulo": "Archivado de Exchange Online para Exchange Server"
    },
    {
        "GUID": "7fc0182e-d107-4556-8329-7caaa511197b",
        "Titulo": "Exchange Online Essentials (ExO P1 Based)"
    },
    {
        "GUID": "e8f81a67-bd96-4074-b108-cf193eb9433b",
        "Titulo": "Exchange Online Essentials"
    },
    {
        "GUID": "80b2d799-d2ba-4d2a-8842-fb0d0f3a4b82",
        "Titulo": "Pantalla completa de Exchange Online"
    },
    {
        "GUID": "f37d5ebf-4bf1-4aa2-8fa3-50c51059e983",
        "Titulo": "Exchange Online (Plan 1) para GCC"
    },
    {
        "GUID": "cb0a98a8-11bc-494c-83d9-c1b1ac65327e",
        "Titulo": "POP de Exchange Online"
    },
    {
        "GUID": "45a2423b-e884-448d-a831-d9e139c52d2f",
        "Titulo": "Exchange Online Protection"
    },
    {
        "GUID": "061f9ace-7d42-4136-88ac-31dc755f143f",
        "Titulo": "Intune"
    },
    {
        "GUID": "d9d89b70-a645-4c24-b041-8d3cb1884ec7",
        "Titulo": "Intune para educación"
    },
    {
        "GUID": "fcecd1f9-a91e-488d-a918-a96cdb6ce2b0",
        "Titulo": "Prueba de usuario de Microsoft Dynamics AX7"
    },
    {
        "GUID": "cb2020b1-d8f6-41c0-9acd-8ff3d6d7831b",
        "Titulo": "Microsoft Azure Multi-Factor Authentication"
    },
    {
        "GUID": "3dd6cf57-d688-4eed-ba52-9e40b5468c3e",
        "Titulo": "Microsoft Defender para Office 365 (Plan 2)"
    },
    {
        "GUID": "b17653a4-2443-4e8c-a550-18249dda78bb",
        "Titulo": "Microsoft 365 A1"
    },
    {
        "GUID": "4b590615-0888-425a-a965-b3bf7789848d",
        "Titulo": "Microsoft 365 A3 para profesores"
    },
    {
        "GUID": "7cfd9a2b-e110-4c39-bf20-c6a3f36a3121",
        "Titulo": "Microsoft 365 A3 para estudiantes"
    },
    {
        "GUID": "18250162-5d87-4436-a834-d795c15c80f3",
        "Titulo": "Beneficios de uso para estudiantes de Microsoft 365 A3"
    },
    {
        "GUID": "32a0e471-8a27-4167-b24f-941559912425",
        "Titulo": "Características de Microsoft 365 A3 Suite para profesores"
    },
    {
        "GUID": "1aa94593-ca12-4254-a738-81a5972958e8",
        "Titulo": "Microsoft 365 A3 - Ventaja para uso de licencia desatendida para alumnos"
    },
    {
        "GUID": "e97c048c-37a4-45fb-ab50-922fbf07a370",
        "Titulo": "Microsoft 365 A5 para profesorado"
    },
    {
        "GUID": "46c119d4-0379-4a9d-85e4-97c66d3f909e",
        "Titulo": "Microsoft 365 A5 para estudiantes"
    },
    {
        "GUID": "31d57bc7-3a05-4867-ab53-97a17835a411",
        "Titulo": "Beneficios de uso para estudiantes de Microsoft 365 A5"
    },
    {
        "GUID": "9b8fe788-6174-4c4e-983b-3330c93ec278",
        "Titulo": "Características de Microsoft 365 A5 Suite para profesores"
    },
    {
        "GUID": "81441ae1-0b31-4185-a6c0-32b6b84d419f",
        "Titulo": "Ventaja para uso de Microsoft 365 A5 sin audioconferencia para alumnos"
    },
    {
        "GUID": "cdd28e44-67e3-425e-be4c-737fab2899d3",
        "Titulo": "Aplicaciones de Microsoft 365 para negocios"
    },
    {
        "GUID": "b214fe43-f5a3-4703-beeb-fa97188220fc",
        "Titulo": "Aplicaciones de Microsoft 365 para negocios"
    },
    {
        "GUID": "c2273bd0-dff7-4215-9ef5-2c7bcfb06425",
        "Titulo": "Aplicaciones de Microsoft 365 para empresas"
    },
    {
        "GUID": "ea4c5ec8-50e3-4193-89b9-50da5bd4cdc7",
        "Titulo": "Aplicaciones de Microsoft 365 para empresas (dispositivo)"
    },
    {
        "GUID": "12b8c807-2e20-48fc-b453-542b6ee9d171",
        "Titulo": "Aplicaciones de Microsoft 365 para profesores"
    },
    {
        "GUID": "c32f9321-a627-406d-a114-1f9c81aaafac",
        "Titulo": "Aplicaciones de Microsoft 365 para estudiantes"
    },
    {
        "GUID": "2d3091c7-0712-488b-b3d8-6b97bde6a1f5",
        "Titulo": "Audioconferencia en Microsoft 365 para GCC"
    },
    {
        "GUID": "df9561a4-4969-4e6a-8e73-c601b68ec077",
        "Titulo": "Audioconferencia de Microsoft 365, pago por minuto (EA)"
    },
    {
        "GUID": "3b555118-da6a-4418-894f-7df1e2096870",
        "Titulo": "Microsoft 365 Empresa Básico"
    },
    {
        "GUID": "dab7782a-93b1-4074-8bb1-0e61318bea0b",
        "Titulo": "Microsoft 365 Empresa Básico"
    },
    {
        "GUID": "f245ecc8-75af-4f8e-b61f-27d8114de5f3",
        "Titulo": "Microsoft 365 Empresa Estándar"
    },
    {
        "GUID": "ac5cef5d-921b-4f97-9ef3-c99076e5470f",
        "Titulo": "Microsoft 365 Business Standard - Prepaid Legacy"
    },
    {
        "GUID": "cbdc14ab-d96c-4c30-b9f4-6ada7cdc1d46",
        "Titulo": "Microsoft 365 Empresa Premium"
    },
    {
        "GUID": "11dee6af-eca8-419f-8061-6864517c1875",
        "Titulo": "Plan de llamadas nacionales de Microsoft 365 (120 minutos)"
    },
    {
        "GUID": "923f58ab-fca1-46a1-92f9-89fda21238a8",
        "Titulo": "Plan de llamadas nacionales de Microsoft 365 para GCC"
    },
    {
        "GUID": "05e9a617-0261-4cee-bb44-138d3ef5d965",
        "Titulo": "Microsoft 365 E3"
    },
    {
        "GUID": "c2ac2ee4-9bb1-47e4-8541-d689c7e83371",
        "Titulo": "Microsoft 365 E3 - Licencia desatendida"
    },
    {
        "GUID": "0c21030a-7e60-4ec7-9a0f-0042e0e0211a",
        "Titulo": "Microsoft 365 E3 (500 puestos mínimo) HUB"
    },
    {
        "GUID": "d61d61cc-f992-433f-a577-5bd016037eeb",
        "Titulo": "Microsoft 365 E3_USGOV_DOD"
    },
    {
        "GUID": "ca9d1dd9-dfe9-4fef-b97c-9bc1ea3c3658",
        "Titulo": "Microsoft 365 E3_USGOV_GCCHIGH"
    },
    {
        "GUID": "06ebc4ee-1bb5-47dd-8120-11324bc54e06",
        "Titulo": "Microsoft 365 E5"
    },
    {
        "GUID": "db684ac5-c0e7-4f92-8284-ef9ebde75d33",
        "Titulo": "Microsoft 365 E5 (500 puestos mínimo) HUB"
    },
    {
        "GUID": "c42b9cae-ea4f-4ab7-9717-81576235ccac",
        "Titulo": "Microsoft 365 E5 Developer (sin Windows y Audioconferencia)"
    },
    {
        "GUID": "184efa21-98c3-4e5d-95ab-d07053a96e67",
        "Titulo": "Cumplimiento de Microsoft 365 E5"
    },
    {
        "GUID": "26124093-3d78-432b-b5dc-48bf992543d5",
        "Titulo": "Seguridad de Microsoft 365 E5"
    },
    {
        "GUID": "44ac31e7-2999-4304-ad94-c948886741d4",
        "Titulo": "Seguridad de Microsoft 365 E5 para EMS E5"
    },
    {
        "GUID": "a91fc4e0-65e5-4266-aa76-4037509c1626",
        "Titulo": "Microsoft 365 E5 con minutos de llamadas"
    },
    {
        "GUID": "cd2925a3-5076-4233-8931-638a8c94f773",
        "Titulo": "Microsoft 365 E5 sin audioconferencia"
    },
    {
        "GUID": "2113661c-6509-4034-98bb-9c47bd28d63c",
        "Titulo": "Microsoft 365 E5 sin audioconferencia (500 puestos mínimo) HUB"
    },
    {
        "GUID": "44575883-256e-4a79-9da4-ebe9acabe2b2",
        "Titulo": "Microsoft 365 F1"
    },
    {
        "GUID": "66b55226-6b4f-492c-910c-a3b7a3c9d993",
        "Titulo": "Microsoft 365 F3"
    },
    {
        "GUID": "91de26be-adfa-4a3d-989e-9131cc23dda7",
        "Titulo": "Complemento de cumplimiento de F5 de Microsoft 365"
    },
    {
        "GUID": "9cfd6bc3-84cd-4274-8a21-8c7c41d6c350",
        "Titulo": "AR DOD_USGOV_DOD del complemento de cumplimiento F5 de Microsoft 365"
    },
    {
        "GUID": "9f436c0e-fb32-424b-90be-6a9f2919d506",
        "Titulo": "AR_USGOV_GCCHIGH de complemento de cumplimiento F5 de Microsoft 365"
    },
    {
        "GUID": "3f17cf90-67a2-4fdb-8587-37c1539507e1",
        "Titulo": "GCC de complemento de cumplimiento F5 de Microsoft 365"
    },
    {
        "GUID": "67ffe999-d9ca-49e1-9d2c-03fb28aa7a48",
        "Titulo": "Complemento de seguridad F5 de Microsoft 365"
    },
    {
        "GUID": "32b47245-eb31-44fc-b945-a8b1576c439f",
        "Titulo": "Complemento de seguridad y cumplimiento de F5 de Microsoft 365"
    },
    {
        "GUID": "f30db892-07e9-47e9-837c-80727f46fd3d",
        "Titulo": "Microsoft Power Automate Gratis"
    },
    {
        "GUID": "99cc8282-2f74-4954-83b7-c6a9a1999067",
        "Titulo": "Características de Microsoft 365 E5 Suite"
    },
    {
        "GUID": "50f60901-3181-4b75-8a2c-4c8e4c1d5a72",
        "Titulo": "Microsoft 365 F1"
    },
    {
        "GUID": "2a914830-d700-444a-b73c-e3f31980d833",
        "Titulo": "Microsoft 365 F3 GCC"
    },
    {
        "GUID": "e823ca47-49c4-46b3-b38d-ca11d5abe3d2",
        "Titulo": "MICROSOFT 365 G3 GCC"
    },
    {
        "GUID": "e2be619b-b125-455f-8660-fb503e431a5d",
        "Titulo": "Microsoft 365 GCC G5"
    },
    {
        "GUID": "9c0587f3-8665-4252-a8ad-b7a5ade57312",
        "Titulo": "Microsoft 365 Lighthouse"
    },
    {
        "GUID": "2347355b-4e81-41a4-9c22-55057a399791",
        "Titulo": "Seguridad y cumplimiento de Microsoft 365 para trabajadores de primera línea"
    },
    {
        "GUID": "726a0894-2c77-4d65-99da-9775ef05aad1",
        "Titulo": "Centro de negocios de Microsoft"
    },
    {
        "GUID": "556640c0-53ea-4773-907d-29c55332983f",
        "Titulo": "Microsoft Cloud para Sustainability vTrial"
    },
    {
        "GUID": "df845ce7-05f9-4894-b5f2-11bbfbcfd2b6",
        "Titulo": "Microsoft Cloud App Security"
    },
    {
        "GUID": "111046dd-295b-4d6d-9724-d52ac90bd1f2",
        "Titulo": "Microsoft Defender para punto de conexión"
    },
    {
        "GUID": "16a55f2f-ff35-4cd5-9146-fb784e3761a5",
        "Titulo": "Microsoft Defender para punto de conexión P1"
    },
    {
        "GUID": "bba890d4-7881-4584-8102-0c3fdfb739a7",
        "Titulo": "Microsoft Defender para punto de conexión P1 para EDU"
    },
    {
        "GUID": "b126b073-72db-4a9d-87a4-b17afe41d4ab",
        "Titulo": "Microsoft Defender para punto de conexión P2_XPLAT"
    },
    {
        "GUID": "509e8ab6-0274-4cda-bcbd-bd164fd562c4",
        "Titulo": "Servidor de Microsoft Defender para punto de conexión"
    },
    {
        "GUID": "26ad4b5c-b686-462e-84b9-d7c22b46837f",
        "Titulo": "Microsoft Defender para Office 365 (Plan 1) Faculty"
    },
    {
        "GUID": "906af65a-2970-46d5-9b58-4e9aa50f0657",
        "Titulo": "Microsoft Dynamics CRM Online Basic"
    },
    {
        "GUID": "98defdf7-f6c1-44f5-a1f6-943b6764e7a5",
        "Titulo": "Microsoft Defender for Identity"
    },
    {
        "GUID": "d0d1ca43-b81a-4f51-81e5-a5b1ad7bb005",
        "Titulo": "Microsoft Defender para Office 365 (Plan 1) GCC"
    },
    {
        "GUID": "56a59ffb-9df1-421b-9e61-8b568583474d",
        "Titulo": "Microsoft Defender para Office 365 (Plan 2) GCC"
    },
    {
        "GUID": "1925967e-8013-495f-9644-c99f8b463748",
        "Titulo": "Administración de vulnerabilidades de Microsoft Defender"
    },
    {
        "GUID": "ad7a56e0-6903-4d13-94f3-5ad491e78960",
        "Titulo": "Complemento de Administración de vulnerabilidades de Microsoft Defender"
    },
    {
        "GUID": "d17b27af-3f49-4822-99f9-56a661538792",
        "Titulo": "Microsoft Dynamics CRM Online"
    },
    {
        "GUID": "ba9a34de-4489-469d-879c-0f0f145321cd",
        "Titulo": "Microsoft Imagine Academy"
    },
    {
        "GUID": "2b317a4a-77a6-4188-9437-b68a77b4e2c6",
        "Titulo": "Dispositivo de Microsoft Intune"
    },
    {
        "GUID": "2c21e77a-e0d6-4570-b38a-7ff2dc17d2ca",
        "Titulo": "Microsoft Intune Device for Government"
    },
    {
        "GUID": "a929cd4d-8672-47c9-8664-159c1f322ba8",
        "Titulo": "Microsoft Intune Suite"
    },
    {
        "GUID": "dcb1a3ae-b33f-4487-846a-a640262fadf4",
        "Titulo": "Prueba de Microsoft Power Apps plan 2"
    },
    {
        "GUID": "4755df59-3f73-41ab-a249-596ad72b5504",
        "Titulo": "Microsoft Power Automate Plan 2"
    },
    {
        "GUID": "e6025b08-2fa5-4313-bd0a-7e5ffca32958",
        "Titulo": "Microsoft Intune SMB"
    },
    {
        "GUID": "5b631642-bd26-49fe-bd20-1daaa972ef80",
        "Titulo": "Microsoft Power Apps para desarrolladores"
    },
    {
        "GUID": "ddfae3e3-fcb2-4174-8ebd-3023cb213c8b",
        "Titulo": "Microsoft Power Apps plan 2 (oferta calificada)"
    },
    {
        "GUID": "4f05b1a3-a978-462c-b93f-781c6bee998f",
        "Titulo": "Soluciones de venta por relación de Microsoft"
    },
    {
        "GUID": "1f2f344a-700d-42c9-9427-5cea1d5d7ba6",
        "Titulo": "Microsoft Stream"
    },
    {
        "GUID": "ec156933-b85b-4c50-84ec-c9e5603709ef",
        "Titulo": "Microsoft Stream plan 2"
    },
    {
        "GUID": "9bd7c846-9556-4453-a542-191d527209e8",
        "Titulo": "Complemento de almacenamiento de Microsoft Stream (500 GB)"
    },
    {
        "GUID": "1c27243e-fb4d-42b1-ae8c-fe25c9616588",
        "Titulo": "Llamada saliente de la audioconferencia de Microsoft Teams con acceso telefónico a EE. UU. y Canadá"
    },
    {
        "GUID": "16ddbbfc-09ea-4de2-b1d7-312db6112d70",
        "Titulo": "Microsoft Teams (Gratis)"
    },
    {
        "GUID": "fde42873-30b6-436b-b361-21af5a6b84ae",
        "Titulo": "Microsoft Teams Essentials"
    },
    {
        "GUID": "3ab6abff-666f-4424-bfb7-f0bc274ec7bc",
        "Titulo": "Microsoft Teams Essentials (Identidad de AAD)"
    },
    {
        "GUID": "710779e8-3d4a-4c88-adb9-386c958d1fdf",
        "Titulo": "Microsoft Teams Exploratory"
    },
    {
        "GUID": "e43b5b99-8dfb-405f-9987-dc307f34bcbd",
        "Titulo": "Teléfono Microsoft Teams Estándar"
    },
    {
        "GUID": "d01d9287-694b-44f3-bcc5-ada78c8d953e",
        "Titulo": "Estándar telefónico de Microsoft Teams para DOD"
    },
    {
        "GUID": "d979703c-028d-4de5-acbf-7955566b69b9",
        "Titulo": "Estándar telefónico de Microsoft Teams para Faculty"
    },
    {
        "GUID": "a460366a-ade7-4791-b581-9fbff1bdaa85",
        "Titulo": "Estándar telefónico de Microsoft Teams para GCC"
    },
    {
        "GUID": "7035277a-5e49-4abc-a24f-0ec49c501bb5",
        "Titulo": "Estándar telefónico de Microsoft Teams para GCCHIGH"
    },
    {
        "GUID": "aa6791d3-bb09-4bc2-afed-c30c3fe26032",
        "Titulo": "Estándar telefónico de Microsoft Teams para pequeñas y medianas empresas"
    },
    {
        "GUID": "1f338bbc-767e-4a1e-a2d4-b73207cc5b93",
        "Titulo": "Estándar telefónico de Microsoft Teams para Estudiante"
    },
    {
        "GUID": "ffaf2d68-1c95-4eb3-9ddd-59b81fba0f61",
        "Titulo": "Estándar telefónico de Microsoft Teams para TELSTRA"
    },
    {
        "GUID": "b0e7de67-e503-4934-b729-53d595ba5cd1",
        "Titulo": "Estándar telefónico de Microsoft Teams para System_USGOV_DOD"
    },
    {
        "GUID": "985fcb26-7b94-475b-b512-89356697be71",
        "Titulo": "Estándar telefónico de Microsoft Teams para USGOV_GCCHIGH"
    },
    {
        "GUID": "440eaaa8-b3e0-484b-a8be-62870b9ba70a",
        "Titulo": "Cuenta de recursos telefónicos de Microsoft Teams"
    },
    {
        "GUID": "2cf22bcb-0c9e-4bc6-8daf-7e7654c0f285",
        "Titulo": "Cuenta de recursos telefónicos de Microsoft Teams para GCC"
    },
    {
        "GUID": "36a0f3b3-adb5-49ea-bf66-762134cf063a",
        "Titulo": "Precio de lanzamiento de Microsoft Teams Premium"
    },
    {
        "GUID": "6af4b3d6-14bb-4a2a-960c-6c902aad34f3",
        "Titulo": "Salas de Microsoft Teams básicas"
    },
    {
        "GUID": "a4e376bd-c61e-4618-9901-3fc0cb1b88bb",
        "Titulo": "Microsoft Teams Rooms Basic para EDU"
    },
    {
        "GUID": "50509a35-f0bd-4c5e-89ac-22f0e16a00f8",
        "Titulo": "Salas de Microsoft Teams básicas sin audioconferencia"
    },
    {
        "GUID": "4cde982a-ede4-4409-9ae6-b003453c8ea6",
        "Titulo": "Salas de Microsoft Teams Pro"
    },
    {
        "GUID": "21943e3a-2429-4f83-84c1-02735cd49e78",
        "Titulo": "Salas de Microsoft Teams Pro sin audioconferencia"
    },
    {
        "GUID": "6070a4c8-34c6-4937-8dfb-39bbc6397a60",
        "Titulo": "Salas de Microsoft Teams Estándar"
    },
    {
        "GUID": "295a8eb0-f78d-45c7-8b5b-1eed5ed02dff",
        "Titulo": "Dispositivos compartidos de Microsoft Teams"
    },
    {
        "GUID": "b1511558-69bd-4e1b-8270-59ca96dba0f3",
        "Titulo": "Dispositivos compartidos de Microsoft Teams para GCC"
    },
    {
        "GUID": "74fbf1bb-47c6-4796-9623-77dc7371723b",
        "Titulo": "Evaluación de Microsoft Teams"
    },
    {
        "GUID": "9fa2f157-c8e4-4351-a3f2-ffa506da1406",
        "Titulo": "Expertos en amenazas de Microsoft: expertos a petición"
    },
    {
        "GUID": "3d957427-ecdc-4df2-aacd-01cc9d519da8",
        "Titulo": "Microsoft Workplace Analytics"
    },
    {
        "GUID": "ba929637-f158-4dee-927c-eb7cdefcd955",
        "Titulo": "Microsoft Viva Goals"
    },
    {
        "GUID": "61902246-d7cb-453e-85cd-53ee28eec138",
        "Titulo": "Microsoft Viva Suite"
    },
    {
        "GUID": "984df360-9a74-4647-8cf8-696749f6247a",
        "Titulo": "Profesores de Educación de Minecraft"
    },
    {
        "GUID": "533b8f26-f74b-4e9c-9c59-50fc4b393b63",
        "Titulo": "Estudiante de Educación de Minecraft"
    },
    {
        "GUID": "84951599-62b7-46f3-9c9d-30551b2ad607",
        "Titulo": "Multi-Geo Capabilities en Office 365"
    },
    {
        "GUID": "aa2695c9-8d59-4800-9dc8-12e01f1735af",
        "Titulo": "Nonprofit Portal"
    },
    {
        "GUID": "94763226-9b3c-4e75-a931-5c89701abe66",
        "Titulo": "Office 365 A1 para profesores"
    },
    {
        "GUID": "78e66a63-337a-4a9a-8959-41c6654dfb56",
        "Titulo": "Office 365 A1 Plus para profesores"
    },
    {
        "GUID": "314c4481-f395-4525-be8b-2ec4bb1e9d91",
        "Titulo": "Office 365 A1 para estudiantes"
    },
    {
        "GUID": "e82ae690-a2d5-4d76-8d30-7c6e01e6022e",
        "Titulo": "Office 365 A1 Plus para estudiantes"
    },
    {
        "GUID": "e578b273-6db4-4691-bba0-8d691f4da603",
        "Titulo": "Office 365 A3 para profesores"
    },
    {
        "GUID": "98b6e773-24d4-4c0d-a968-6e787a1f8204",
        "Titulo": "Office 365 A3 para estudiantes"
    },
    {
        "GUID": "a4585165-0533-458a-97e3-c400570268c4",
        "Titulo": "Office 365 A5 para profesores"
    },
    {
        "GUID": "ee656612-49fa-43e5-b67e-cb1fdf7699df",
        "Titulo": "Office 365 A5 para estudiantes"
    },
    {
        "GUID": "1b1b1f7a-8355-43b6-829f-336cfccb744c",
        "Titulo": "Cumplimiento avanzado de Office 365"
    },
    {
        "GUID": "4ef96642-f096-40de-a3e9-d83fb2f90211",
        "Titulo": "Microsoft Defender for Office 365 (Plan 1)"
    },
    {
        "GUID": "e5788282-6381-469f-84f0-3d7d4021d34d",
        "Titulo": "Office 365 Extra File Storage para GCC"
    },
    {
        "GUID": "29a2f828-8f39-4837-b8ff-c957e86abe3c",
        "Titulo": "Nube comercial de Microsoft Teams"
    },
    {
        "GUID": "84d5f90f-cd0d-4864-b90b-1c7ba63b4808",
        "Titulo": "Office 365 Cloud App Security"
    },
    {
        "GUID": "99049c9c-6011-4908-bf17-15f496e6519d",
        "Titulo": "Office 365 Extra File Storage"
    },
    {
        "GUID": "18181a46-0d4e-45cd-891e-60aabd171b4e",
        "Titulo": "Office 365 E1"
    },
    {
        "GUID": "6634e0ce-1a9f-428c-a498-f84ec7b8aa2e",
        "Titulo": "Office 365 E2"
    },
    {
        "GUID": "6fd2c87f-b296-42f0-b197-1e91e994b900",
        "Titulo": "Office 365 E3"
    },
    {
        "GUID": "189a915c-fe4f-4ffa-bde4-85b9628d07a0",
        "Titulo": "Office 365 E3 Developer"
    },
    {
        "GUID": "b107e5a3-3e60-4c0d-a184-a7e4395eb44c",
        "Titulo": "Office 365 E3_USGOV_DOD"
    },
    {
        "GUID": "aea38a85-9bd5-4981-aa00-616b411205bf",
        "Titulo": "Office 365 E3_USGOV_GCCHIGH"
    },
    {
        "GUID": "1392051d-0cb9-4b7a-88d5-621fee5e8711",
        "Titulo": "Office 365 E4"
    },
    {
        "GUID": "c7df2760-2c81-4ef7-b578-5b5392b571df",
        "Titulo": "Office 365 E5"
    },
    {
        "GUID": "26d45bd9-adf1-46cd-a9e1-51e9a5524128",
        "Titulo": "Office 365 E5 sin audioconferencia"
    },
    {
        "GUID": "4b585984-651b-448a-9e53-3b10f069cf7f",
        "Titulo": "Office 365 F3"
    },
    {
        "GUID": "3f4babde-90ec-47c6-995d-d223749065d1",
        "Titulo": "Office 365 G1 GCC"
    },
    {
        "GUID": "535a3a29-c5f0-42fe-8215-d3b9e1f38c4a",
        "Titulo": "Office 365 G3 GCC"
    },
    {
        "GUID": "8900a2c0-edba-4079-bdf3-b276e293b6a8",
        "Titulo": "Office 365 G5 GCC"
    },
    {
        "GUID": "1a585bba-1ce3-416e-b1d6-9c482b52fcf6",
        "Titulo": "Cumplimiento avanzado de Office 365 para GCC"
    },
    {
        "GUID": "04a7fb0d-32e0-4241-b4f5-3f7618cd1162",
        "Titulo": "Office 365 Mediana empresa"
    },
    {
        "GUID": "bd09678e-b83c-4d3f-aaba-3dad4abd128b",
        "Titulo": "OFFICE 365 Pequeña empresa"
    },
    {
        "GUID": "fc14ec4a-4169-49a4-a51e-2c852931814b",
        "Titulo": "Office 365 Pequeña Empresa Premium"
    },
    {
        "GUID": "e6778190-713e-4e4f-9119-8b8238de25df",
        "Titulo": "OneDrive para la empresa (Plan 1)"
    },
    {
        "GUID": "ed01faf2-1d88-4947-ae91-45ca18703a96",
        "Titulo": "OneDrive para la empresa (Plan 2)"
    },
    {
        "GUID": "87bbbc60-4754-4998-8c88-227dca264858",
        "Titulo": "Power Apps and Logic Flows"
    },
    {
        "GUID": "bf666882-9c9b-4b2e-aa2f-4789b0a52ba2",
        "Titulo": "Acceso de línea de base a PowerApps por aplicación"
    },
    {
        "GUID": "a8ad7d2b-b8cf-49d6-b25a-69094a0be206",
        "Titulo": "Plan de Power Apps por aplicación"
    },
    {
        "GUID": "b4d7b828-e8dc-4518-91f9-e123ae48440d",
        "Titulo": "Power Apps por plan de aplicación (1 aplicación o portal)"
    },
    {
        "GUID": "b30411f5-fea1-4a59-9ad9-3db7c7ead579",
        "Titulo": "Plan de Power Apps por usuario"
    },
    {
        "GUID": "8e4c6baa-f2ff-4884-9c38-93785d0d7ba1",
        "Titulo": "Plan de Power Apps por usuario para la administración pública"
    },
    {
        "GUID": "eca22b68-b31f-4e9c-a20c-4d40287bc5dd",
        "Titulo": "Power Apps Plan 1 para la administración pública"
    },
    {
        "GUID": "57f3babd-73ce-40de-bcb2-dadbfbfff9f7",
        "Titulo": "Complemento de capacidad de inicio de sesión en los portales de Power Apps Nivel 2 (10 unidades mínimo)"
    },
    {
        "GUID": "26c903d5-d385-4cb1-b650-8d81a643b3c4",
        "Titulo": "Complemento de capacidad de inicio de sesión en los portales de Power Apps Nivel 2 (10 unidades mín.) para la administración pública"
    },
    {
        "GUID": "927d8402-8d3b-40e8-b779-34e859f7b497",
        "Titulo": "Complemento de capacidad de inicio de sesión en los portales de Power Apps Nivel 3 (50 unidades mínimo)"
    },
    {
        "GUID": "a0de5e3a-2500-4a19-b8f4-ec1c64692d22",
        "Titulo": "Complemento de capacidad de la vista de página de los portales de Power Apps"
    },
    {
        "GUID": "15a64d3e-5b99-4c4b-ae8f-aa6da264bfe7",
        "Titulo": "Complemento de capacidad de la vista de página de los portales de Power Apps para la administración pública"
    },
    {
        "GUID": "b3a42176-0a8c-4c3f-ba4e-f2b37fe5be6b",
        "Titulo": "Power Automate por plan de flujo"
    },
    {
        "GUID": "4a51bf65-409c-4a91-b845-1121b571cc9d",
        "Titulo": "Plan de Power Automate por usuario"
    },
    {
        "GUID": "d80a4c5d-8f05-4b64-9926-6574b9e6aee4",
        "Titulo": "Plan de Power Automate por usuario (departamento)"
    },
    {
        "GUID": "c8803586-c136-479a-8ff3-f5f32d23a68e",
        "Titulo": "Plan por usuario de Power Automate para la administración pública"
    },
    {
        "GUID": "eda1941c-3c4f-4995-b5eb-e85a42175ab9",
        "Titulo": "Plan de Power Automate por usuario con RPA atendido"
    },
    {
        "GUID": "2b3b0c87-36af-4d15-8124-04a691cc2546",
        "Titulo": "Power Automate Plan 1 para la administración pública (oferta calificada)"
    },
    {
        "GUID": "3539d28c-6e35-4a30-b3a9-cd43d5d3e0e2",
        "Titulo": "Complemento RPA desatendido de Power Automate"
    },
    {
        "GUID": "e2767865-c3c9-4f09-9f99-6eee6eef861a",
        "Titulo": "Power BI"
    },
    {
        "GUID": "a403ebcc-fae0-4ca2-8c8c-7a907fd6c235",
        "Titulo": "Power BI (gratis)"
    },
    {
        "GUID": "45bc2c81-6072-436a-9b0b-3b12eefbc402",
        "Titulo": "Complemento de Power BI para Office 365"
    },
    {
        "GUID": "7b26f5ab-a763-4c00-a1ac-f6c4b5506945",
        "Titulo": "Power BI Premium P1"
    },
    {
        "GUID": "c1d032e0-5619-4761-9b5c-75b6831e1711",
        "Titulo": "Power BI Premium por usuario"
    },
    {
        "GUID": "de376a03-6e5b-42ec-855f-093fb50b8ca5",
        "Titulo": "Complemento de Power BI Premium por usuario"
    },
    {
        "GUID": "060d8061-f606-4e69-a4e7-e8fff75ea1f5",
        "Titulo": "Power BI Premium por usuario para profesores"
    },
    {
        "GUID": "f168a3fb-7bcf-4a27-98c3-c235ea4b78b4",
        "Titulo": "Power BI Premium por usuario (departamento)"
    },
    {
        "GUID": "f8a1db68-be16-40ed-86d5-cb42ce701560",
        "Titulo": "Power BI Pro"
    },
    {
        "GUID": "420af87e-8177-4146-a780-3786adaffbca",
        "Titulo": "Power BI Pro CE"
    },
    {
        "GUID": "3a6a908c-09c5-406a-8170-8ebb63c42882",
        "Titulo": "Power BI Pro (departamento)"
    },
    {
        "GUID": "de5f128b-46d7-4cfc-b915-a89ba060ea56",
        "Titulo": "Power BI Pro para profesores"
    },
    {
        "GUID": "f0612879-44ea-47fb-baf0-3d76d9235576",
        "Titulo": "Power BI Pro para GCC"
    },
    {
        "GUID": "3f9f06f5-3c31-472c-985f-62d9c10ec167",
        "Titulo": "Power Pages vTrial para creadores"
    },
    {
        "GUID": "e4e55366-9635-46f4-a907-fc8c3b5ec81f",
        "Titulo": "Power Virtual Agent"
    },
    {
        "GUID": "4b74a65c-8b4a-4fc8-9f6b-5177ed11ddfa",
        "Titulo": "Licencia de usuario de Power Virtual Agent"
    },
    {
        "GUID": "606b54a9-78d8-4298-ad8b-df6ef4481c80",
        "Titulo": "Prueba de Power Virtual Agents Viral"
    },
    {
        "GUID": "e42bc969-759a-4820-9283-6b73085b68e6",
        "Titulo": "Administración de privacidad: riesgo"
    },
    {
        "GUID": "dcdbaae7-d8c9-40cb-8bb1-62737b9e5a86",
        "Titulo": "Privacy Management: riesgo para EDU"
    },
    {
        "GUID": "046f7d3b-9595-4685-a2e8-a2832d2b26aa",
        "Titulo": "Administración de privacidad: GCC de riesgo"
    },
    {
        "GUID": "83b30692-0d09-435c-a455-2ab220d504b9",
        "Titulo": "Administración de privacidad: risk_USGOV_DOD"
    },
    {
        "GUID": "787d7e75-29ca-4b90-a3a9-0b780b35367c",
        "Titulo": "Administración de privacidad: risk_USGOV_GCCHIGH"
    },
    {
        "GUID": "d9020d1c-94ef-495a-b6de-818cbbcaa3b8",
        "Titulo": "Privacy Management: solicitud de derechos del firmante (1)"
    },
    {
        "GUID": "475e3e81-3c75-4e07-95b6-2fed374536c8",
        "Titulo": "Privacy Management: solicitud de derechos del firmante (1) para EDU"
    },
    {
        "GUID": "017fb6f8-00dd-4025-be2b-4eff067cae72",
        "Titulo": "Administración de privacidad: GCC de solicitud de derechos del firmante (1)"
    },
    {
        "GUID": "d3c841f3-ea93-4da2-8040-6f2348d20954",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (1) USGOV_DOD"
    },
    {
        "GUID": "706d2425-6170-4818-ba08-2ad8f1d2d078",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (1) USGOV_GCCHIGH"
    },
    {
        "GUID": "78ea43ac-9e5d-474f-8537-4abb82dafe27",
        "Titulo": "Privacy Management: solicitud de derechos del firmante (10)"
    },
    {
        "GUID": "e001d9f1-5047-4ebf-8927-148530491f83",
        "Titulo": "Privacy Management: solicitud de derechos del firmante (10) para EDU"
    },
    {
        "GUID": "a056b037-1fa0-4133-a583-d05cff47d551",
        "Titulo": "Administración de privacidad: GCC de solicitud de derechos del firmante (10)"
    },
    {
        "GUID": "ab28dfa1-853a-4f54-9315-f5146975ac9a",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (10) USGOV_DOD"
    },
    {
        "GUID": "f6aa3b3d-62f4-4c1d-a44f-0550f40f729c",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (10) USGOV_GCCHIGH"
    },
    {
        "GUID": "c416b349-a83c-48cb-9529-c420841dedd6",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (50)"
    },
    {
        "GUID": "f6c82f13-9554-4da1-bed3-c024cc906e02",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (50)"
    },
    {
        "GUID": "ed45d397-7d61-4110-acc0-95674917bb14",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (50) para EDU"
    },
    {
        "GUID": "cf4c6c3b-f863-4940-97e8-1d25e912f4c4",
        "Titulo": "Privacy Management: solicitud de derechos del firmante (100)"
    },
    {
        "GUID": "9b85b4f0-92d9-4c3d-b230-041520cb1046",
        "Titulo": "Privacy Management: solicitud de derechos del firmante (100) para EDU"
    },
    {
        "GUID": "91bbc479-4c2c-4210-9c88-e5b468c35b83",
        "Titulo": "Administración de privacidad: GCC de solicitud de derechos del firmante (100)"
    },
    {
        "GUID": "ba6e69d5-ba2e-47a7-b081-66c1b8e7e7d4",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (100) USGOV_DOD"
    },
    {
        "GUID": "cee36ce4-cc31-481f-8cab-02765d3e441f",
        "Titulo": "Administración de privacidad: solicitud de derechos del firmante (100) USGOV_GCCHIGH"
    },
    {
        "GUID": "a10d5e58-74da-4312-95c8-76be4e5b75a0",
        "Titulo": "Project para Office 365"
    },
    {
        "GUID": "776df282-9fc0-4862-99e2-70e561b9909e",
        "Titulo": "Project Online Essentials"
    },
    {
        "GUID": "e433b246-63e7-4d0b-9efa-7940fa3264d6",
        "Titulo": "Project Online Essentials para profesores"
    },
    {
        "GUID": "ca1a159a-f09e-42b8-bb82-cb6420f54c8e",
        "Titulo": "Project Online Essentials para GCC"
    },
    {
        "GUID": "09015f9f-377f-4538-bbb5-f75ceb09358a",
        "Titulo": "Project Online Premium"
    },
    {
        "GUID": "2db84718-652c-47a7-860c-f10d8abbdae3",
        "Titulo": "Project Online Premium sin Project Client"
    },
    {
        "GUID": "f82a60b8-1ee3-4cfb-a4fe-1c6a53c2656c",
        "Titulo": "Project Online con Project para Office 365"
    },
    {
        "GUID": "beb6439c-caad-48d3-bf46-0c82871e12be",
        "Titulo": "Project plan 1"
    },
    {
        "GUID": "84cd610f-a3f8-4beb-84ab-d9d2c902c6c9",
        "Titulo": "Project Plan 1 (para departamento)"
    },
    {
        "GUID": "53818b1b-4a27-454b-8896-0dba576410e6",
        "Titulo": "Project plan 3"
    },
    {
        "GUID": "46102f44-d912-47e7-b0ca-1bd7b70ada3b",
        "Titulo": "Project plan 3 (para departamento)"
    },
    {
        "GUID": "46974aed-363e-423c-9e6a-951037cec495",
        "Titulo": "Plan del proyecto 3 para profesores"
    },
    {
        "GUID": "074c6829-b3a0-430a-ba3d-aca365e57065",
        "Titulo": "Plan del proyecto 3 para GCC"
    },
    {
        "GUID": "f2230877-72be-4fec-b1ba-7156d6f75bd6",
        "Titulo": "Plan del proyecto 5 para GCC"
    },
    {
        "GUID": "b732e2a7-5694-4dff-a0f2-9d9204c794ac",
        "Titulo": "Plan del proyecto 5 sin el cliente de proyecto para los profesores"
    },
    {
        "GUID": "8c4ce438-32a7-4ac5-91a6-e22ae08d9c8b",
        "Titulo": "Rights Management adhoc"
    },
    {
        "GUID": "093e8d14-a334-43d9-93e3-30589a8b47d0",
        "Titulo": "Rights Management Service Basic Content Protection"
    },
    {
        "GUID": "08e18479-4483-4f70-8f17-6f92156d8ea9",
        "Titulo": "Complemento de máquinas adicionales para Sensor Data Intelligence para Dynamics 365 Supply Chain Management"
    },
    {
        "GUID": "9ea4bdef-a20b-4668-b4a7-73e1f7696e0a",
        "Titulo": "Complemento de escenario de Sensor Data Intelligence para Dynamics 365 Supply Chain Management"
    },
    {
        "GUID": "1fc08a02-8b3d-43b9-831e-f76859e04e1a",
        "Titulo": "SharePoint Online (Plan 1)"
    },
    {
        "GUID": "a9732ec9-17d9-494c-a51c-d6b45b384dcb",
        "Titulo": "SharePoint Online (Plan 2)"
    },
    {
        "GUID": "f61d4aba-134f-44e9-a2a0-f81a5adb26e4",
        "Titulo": "SharePoint Syntex"
    },
    {
        "GUID": "b8b749f8-a4ef-4887-9539-c95b1eaa5db7",
        "Titulo": "Skype empresarial online (Plan 1)"
    },
    {
        "GUID": "d42c793f-6c78-4f43-92ca-e8f6a02b035f",
        "Titulo": "Skype empresarial online (Plan 2)"
    },
    {
        "GUID": "d3b4fe1f-9992-4930-8acb-ca6ec609365e",
        "Titulo": "Llamadas RTC nacionales e internacionales de Skype empresarial"
    },
    {
        "GUID": "0dab259f-bf13-4952-b7f8-7db8f131b28d",
        "Titulo": "Llamadas RTC nacionales de Skype empresarial"
    },
    {
        "GUID": "54a152dc-90de-4996-93d2-bc47e670fc06",
        "Titulo": "Llamadas RTC nacionales de Skype empresarial (120 minutos)"
    },
    {
        "GUID": "06b48c5f-01d9-4b18-9015-03b52040f51a",
        "Titulo": "Plan de llamadas de uso de RTC de Skype Empresarial"
    },
    {
        "GUID": "ae2343d1-0999-43f6-ae18-d816516f6e78",
        "Titulo": "Teléfono Teams con plan de llamadas"
    },
    {
        "GUID": "de3312e1-c7b0-46e6-a7c3-a515ff90bc86",
        "Titulo": "Llamadas de TELSTRA para O365"
    },
    {
        "GUID": "9f3d9c1d-25a5-4aaa-8e59-23a1e6450a67",
        "Titulo": "Impresión universal"
    },
    {
        "GUID": "ca7f3140-d88c-455b-9a1c-7f0679e31a76",
        "Titulo": "Visio plan 1"
    },
    {
        "GUID": "38b434d2-a15e-4cde-9a98-e737c75623e1",
        "Titulo": "Visio plan 2"
    },
    {
        "GUID": "4b244418-9658-4451-a2b8-b5e2b364e9bd",
        "Titulo": "Visio Online Plan 1"
    },
    {
        "GUID": "bf95fd32-576a-4742-8d7a-6dc4940b9532",
        "Titulo": "Plan de Visio 2 para los profesores"
    },
    {
        "GUID": "c5928f49-12ba-48f7-ada3-0d743a3601d5",
        "Titulo": "Visio Online Plan 2"
    },
    {
        "GUID": "4ae99959-6b0f-43b0-b1ce-68146001bdba",
        "Titulo": "Visio Plan 2 para GCC"
    },
    {
        "GUID": "4016f256-b063-4864-816e-d818aad600c9",
        "Titulo": "Temas Viva"
    },
    {
        "GUID": "1e7e1070-8ccb-4aca-b470-d7cb538cb07e",
        "Titulo": "Windows 10/11 Enterprise E5 (Original)"
    },
    {
        "GUID": "8efbe2f6-106e-442f-97d4-a59aa6037e06",
        "Titulo": "Windows 10/11 Enterprise A3 para profesores"
    },
    {
        "GUID": "d4ef921e-840b-4b48-9a90-ab6698bc7b31",
        "Titulo": "Windows 10/11 Enterprise A3 para estudiantes"
    },
    {
        "GUID": "7b1a89a9-5eb9-4cf8-9467-20c943f1122c",
        "Titulo": "Windows 10/11 Enterprise A5 para profesores"
    },
    {
        "GUID": "cb10e6cd-9da4-4992-867b-67546b1db821",
        "Titulo": "WINDOWS 10/11 ENTERPRISE E3"
    },
    {
        "GUID": "6a0f6da5-0b87-4190-a6ae-9bb5a2b9546a",
        "Titulo": "WINDOWS 10/11 ENTERPRISE E3"
    },
    {
        "GUID": "488ba24a-39a9-4473-8ee5-19291e71b002",
        "Titulo": "Windows 10/11 Enterprise E5"
    },
    {
        "GUID": "938fd547-d794-42a4-996c-1cc206619580",
        "Titulo": "Windows 10/11 Enterprise E5 Commercial (compatible con GCC)"
    },
    {
        "GUID": "d13ef257-988a-46f3-8fce-f47484dd4550",
        "Titulo": "Windows 10/11 Enterprise VDA"
    },
    {
        "GUID": "816eacd3-e1e3-46b3-83c8-1ffd37e053d9",
        "Titulo": "Windows 365 Business, 1 vCPU, 2 GB, 64 GB"
    },
    {
        "GUID": "135bee78-485b-4181-ad6e-40286e311850",
        "Titulo": "Windows 365 Business, 2 vCPU, 4 GB, 128 GB"
    },
    {
        "GUID": "805d57c3-a97d-4c12-a1d0-858ffe5015d0",
        "Titulo": "Windows 365 Business, 2 vCPU, 4 GB, 256 GB"
    },
    {
        "GUID": "42e6818f-8966-444b-b7ac-0027c83fa8b5",
        "Titulo": "Windows 365 Business, 2 vCPU, 4 GB, 64 GB"
    },
    {
        "GUID": "71f21848-f89b-4aaa-a2dc-780c8e8aac5b",
        "Titulo": "Windows 365 Business, 2 vCPU, 8 GB, 128 GB"
    },
    {
        "GUID": "750d9542-a2f8-41c7-8c81-311352173432",
        "Titulo": "Windows 365 Business, 2 vCPU, 8 GB, 256 GB"
    },
    {
        "GUID": "ad83ac17-4a5a-4ebb-adb2-079fb277e8b9",
        "Titulo": "Windows 365 Business, 4 vCPU, 16 GB, 128 GB"
    },
    {
        "GUID": "439ac253-bfbc-49c7-acc0-6b951407b5ef",
        "Titulo": "Windows 365 Business, 4 vCPU, 16 GB, 128 GB (con Ventaja híbrida de Windows)"
    },
    {
        "GUID": "b3891a9f-c7d9-463c-a2ec-0b2321bda6f9",
        "Titulo": "Windows 365 Business, 4 vCPU, 16 GB, 256 GB"
    },
    {
        "GUID": "1b3043ad-dfc6-427e-a2c0-5ca7a6c94a2b",
        "Titulo": "Windows 365 Business, 4 vCPU, 16 GB, 512 GB"
    },
    {
        "GUID": "3cb45fab-ae53-4ff6-af40-24c1915ca07b",
        "Titulo": "Windows 365 Business, 8 vCPU, 32 GB, 128 GB"
    },
    {
        "GUID": "fbc79df2-da01-4c17-8d88-17f8c9493d8f",
        "Titulo": "Windows 365 Business, 8 vCPU, 32 GB, 256 GB"
    },
    {
        "GUID": "8ee402cd-e6a8-4b67-a411-54d1f37a2049",
        "Titulo": "Windows 365 Business, 8 vCPU, 32 GB, 512 GB"
    },
    {
        "GUID": "0c278af4-c9c1-45de-9f4b-cd929e747a2c",
        "Titulo": "Windows 365 Enterprise, 1 vCPU, 2 GB, 64 GB"
    },
    {
        "GUID": "226ca751-f0a4-4232-9be5-73c02a92555e",
        "Titulo": "Windows 365 Enterprise, 2 vCPU, 4 GB, 128 GB"
    },
    {
        "GUID": "5265a84e-8def-4fa2-ab4b-5dc278df5025",
        "Titulo": "Windows 365 Enterprise, 2 vCPU, 4 GB, 256 GB"
    },
    {
        "GUID": "7bb14422-3b90-4389-a7be-f1b745fc037f",
        "Titulo": "Windows 365 Enterprise, 2 vCPU, 4 GB, 64 GB"
    },
    {
        "GUID": "e2aebe6c-897d-480f-9d62-fff1381581f7",
        "Titulo": "Windows 365 Enterprise, 2 vCPU, 8 GB, 128 GB"
    },
    {
        "GUID": "1c79494f-e170-431f-a409-428f6053fa35",
        "Titulo": "Windows 365 Enterprise, 2 vCPU, 8 GB, 256 GB"
    },
    {
        "GUID": "d201f153-d3b2-4057-be2f-fe25c8983e6f",
        "Titulo": "Windows 365 Enterprise, 4 vCPU, 16 GB, 128 GB"
    },
    {
        "GUID": "96d2951e-cb42-4481-9d6d-cad3baac177e",
        "Titulo": "Windows 365 Enterprise, 4 vCPU, 16 GB, 256 GB"
    },
    {
        "GUID": "0da63026-e422-4390-89e8-b14520d7e699",
        "Titulo": "Windows 365 Enterprise, 4 vCPU, 16 GB, 512 GB"
    },
    {
        "GUID": "c97d00e4-0c4c-4ec2-a016-9448c65de986",
        "Titulo": "Windows 365 Enterprise, 8 vCPU, 32 GB, 128 GB"
    },
    {
        "GUID": "7818ca3e-73c8-4e49-bc34-1276a2d27918",
        "Titulo": "Windows 365 Enterprise, 8 vCPU, 32 GB, 256 GB"
    },
    {
        "GUID": "9fb0ba5f-4825-4e84-b239-5167a3a5d4dc",
        "Titulo": "Windows 365 Enterprise, 8 vCPU, 32 GB, 512 GB"
    },
    {
        "GUID": "bce09f38-1800-4a51-8d50-5486380ba84a",
        "Titulo": "Windows 365 Enterprise 2 vCPU, 4 GB, 128 GB (Versión preliminar)"
    },
    {
        "GUID": "1f9990ca-45d9-4c8d-8d04-a79241924ce1",
        "Titulo": "Windows 365 de uso compartido, 2 vCPU, 4 GB, 64 GB"
    },
    {
        "GUID": "90369797-7141-4e75-8f5e-d13f4b6092c1",
        "Titulo": "Windows 365 de uso compartido, 2 vCPU, 4 GB, 128 GB"
    },
    {
        "GUID": "8fe96593-34d3-49bb-aeee-fb794fed0800",
        "Titulo": "Windows 365 de uso compartido, 2 vCPU, 4 GB, 256 GB"
    },
    {
        "GUID": "2d21fc84-b918-491e-ad84-e24d61ccec94",
        "Titulo": "Windows 365 de uso compartido, 2 vCPU, 8 GB, 128 GB"
    },
    {
        "GUID": "2eaa4058-403e-4434-9da9-ea693f5d96dc",
        "Titulo": "Windows 365 de uso compartido, 2 vCPU, 8 GB, 256 GB"
    },
    {
        "GUID": "1bf40e76-4065-4530-ac37-f1513f362f50",
        "Titulo": "Windows 365 de uso compartido, 4 vCPU, 16 GB, 128 GB"
    },
    {
        "GUID": "a9d1e0df-df6f-48df-9386-76a832119cca",
        "Titulo": "Windows 365 de uso compartido, 4 vCPU, 16 GB, 256 GB"
    },
    {
        "GUID": "469af4da-121c-4529-8c85-9467bbebaa4b",
        "Titulo": "Windows 365 de uso compartido, 4 vCPU, 16 GB, 512 GB"
    },
    {
        "GUID": "f319c63a-61a9-42b7-b786-5695bc7edbaf",
        "Titulo": "Windows 365 de uso compartido, 8 vCPU, 32 GB, 128 GB"
    },
    {
        "GUID": "fb019e88-26a0-4218-bd61-7767d109ac26",
        "Titulo": "Windows 365 de uso compartido, 8 vCPU, 32 GB, 256 GB"
    },
    {
        "GUID": "f4dc1de8-8c94-4d37-af8a-1fca6675590a",
        "Titulo": "Windows 365 de uso compartido, 8 vCPU, 32 GB, 512 GB"
    },
    {
        "GUID": "6470687e-a428-4b7a-bef2-8a291ad947c9",
        "Titulo": "Tienda Windows para empresas"
    },
    {
        "GUID": "c7e9d9e6-1981-4bf3-bb50-a5bdfaa06fb2",
        "Titulo": "Tienda Windows para Business EDU Faculty"
    }
    ]"""
    licences_dict=json.loads(licences)
    return licences_dict

def get_antepenultimateBusinessDay():
    d=datetime.now()
    offset = BMonthEnd()
    #Last day of current month
    lastDay=offset.rollforward(d)
    antepenultimateBusinessDay=lastDay
    #Monday=0, Sunday=6
    weekday=lastDay.weekday()
    if(weekday>=2 or weekday<=4):
        antepenultimateBusinessDay=(lastDay + timedelta(days=-2))
    elif(weekday==0 or weekday==1 or weekday==6):
        antepenultimateBusinessDay=(lastDay + timedelta(days=-4))
    elif(weekday==5):
        antepenultimateBusinessDay=(lastDay + timedelta(days=-3))
    d="%02d/%02d/%d" % (d.month, d.day, d.year)
    antepenultimateBusinessDay="%02d/%02d/%d" % (antepenultimateBusinessDay.month, antepenultimateBusinessDay.day, antepenultimateBusinessDay.year) 

    return d==antepenultimateBusinessDay


def get_userLicensesReport():
    
    if(get_antepenultimateBusinessDay()==False):
        #Sharepoint.get_listItems('MSFT','Usuarios activos'))        
        users=asyncio.run(User.get_assignedLicenses())
        for x in users:
            assignedLicenses=x['assignedLicenses']
            productName=''
            for y in assignedLicenses:
                output_dict = [x for x in get_licences() if x['GUID'] == y['skuId']]
                productName=productName+output_dict[0]['Titulo']



get_userLicensesReport()