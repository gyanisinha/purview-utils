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

entities = reader.parse_column_mapping('./custom_process_column_lineage.xlsx')

results = client.upload_entities(entities)


print(json.dumps(results, indent=2))
