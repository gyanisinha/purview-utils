import json
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core.client import PurviewClient
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader

auth = ServicePrincipalAuthentication(
    tenant_id = "<enter value>",
    client_id = "<enter value>",
    client_secret = "<enter value>"
)
client = PurviewClient(
    account_name= "<enter value>",
    authentication = auth
)

ec = ExcelConfiguration()
reader = ExcelReader(ec)

entityTypeDefs = reader.parse_entity_defs('./custom_process.xlsx')

results = client.upload_typedefs(entityTypeDefs)

print(json.dumps(results, indent=2))
