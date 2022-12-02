import json
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core.client import PurviewClient
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader

auth = ServicePrincipalAuthentication(
    client_id="<enter value>",
    tenant_id="<enter value>",    
    client_secret="<enter value>"
)
client = PurviewClient(
    account_name= "<enter value>",
    authentication = auth
)


ec = ExcelConfiguration()
reader = ExcelReader(ec)

entities = reader.parse_bulk_entities("./BulkUpdateMissingSchema_tables.xlsx") #path to the input file

results = client.upload_entities(entities)

print(json.dumps(results, indent=2))
