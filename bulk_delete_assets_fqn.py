import openpyxl
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader
import json
import os,sys
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient, AtlasEntity, AtlasProcess
from pyapacheatlas.core.util import GuidTracker

if __name__ == "__main__":
    purview_Account_Name = "<enter value>"
    oauth = ServicePrincipalAuthentication(
    client_id="<enter value>",
    tenant_id="<enter value>",    
    client_secret="<enter value>"
    )
    client = PurviewClient(
        account_name=purview_Account_Name,
        authentication=oauth
    )


ec = ExcelConfiguration() 
reader = ExcelReader(ec)

#provide the path of excel file which ahs list of fqns with header as "qualifiedName" and sheet name as "BulkEntities
wb = openpyxl.load_workbook('./list_of_assets_to_be_deleted.xlsx',data_only=True)
sheet = wb['BulkEntities']
rows = reader._parse_spreadsheet(sheet)
batch = []

for row in rows:
    qualifiedName=row["qualifiedName"]
    # print(qualifiedName)
    filter_setup = {              
                       "attributeName": "qualifiedName",
                       "operator": "eq",
                       "attributeValue": qualifiedName
                   }

    query = client.discovery.query(filter=filter_setup)

    batch.append(query["value"][0]["id"])

print(batch)

for item in batch:    
    if len(batch) > 0:
        client.delete_entity(guid=batch)

