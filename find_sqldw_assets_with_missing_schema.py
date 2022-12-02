import json
import os
# PyApacheAtlas packages
# Connect to Atlas via a Service Principal
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient  # Communicate with your Atlas server


if __name__ == "__main__":
    """
    This sample provides an example of deleting an entity through the Atlas API.
    """

    # Authenticate against your Atlas server

    oauth = ServicePrincipalAuthentication(
        tenant_id=os.environ.get("TENANT_ID", "<enter tenant id>"),
        client_id=os.environ.get("CLIENT_ID", "<enter client id of the service principal (application id)>"),
        client_secret=os.environ.get("CLIENT_SECRET", "<enter client secret")
    )

    client = PurviewClient(
        account_name = os.environ.get("PURVIEW_NAME", "<enter purview account name>"),
        authentication=oauth
    )

    # Note: modify the filter_setup as necessary    
    
    limit = 1000 #to search upto 1000 assets
    # collection_id = "<enter value>"
    # filter_setup = {"and": [{"collectionId": collection_id}, {"assetType": "Azure Data Lake Storage Gen2"}]}

    filter_setup = {"assetType": "Azure SQL Data Warehouse"}
    query = client.discovery.query(limit=limit, filter=filter_setup)
    
    query_list = []
    batch = []

    for entry in query["value"]:      
        query_list.append(entry["id"])

    print("Total #assets searched:", len(query_list))

    print("\nAssets with missing schema:")

    start = 0
    end = len(query_list)
    batch_size = 100

    for iter in range(start, end, batch_size):
        batch = query_list[iter:iter+batch_size]
        response = client.get_entity(batch)
        # print(response['entities'])
        
        for item in response['entities']:

            if (item['typeName'] == "azure_sql_dw_table" or item['typeName'] == "azure_sql_dw_view"):
                valid = item['relationshipAttributes'].get("columns")
                if (valid and bool(item['relationshipAttributes']['columns'])):
                    # print(item['relationshipAttributes']['columns'])
                    pass
                else:
                    print(item['attributes']['qualifiedName'])
                    
    print("Done")
