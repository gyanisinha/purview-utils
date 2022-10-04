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
        tenant_id=os.environ.get("TENANT_ID", "<enter value>"),
        client_id=os.environ.get("CLIENT_ID", "<enter value>"),
        client_secret=os.environ.get("CLIENT_SECRET", "<enter value>")
    )

    client = PurviewClient(
        account_name = os.environ.get("PURVIEW_NAME", "<enter value>"),
        authentication=oauth
    )

    #modify the filter_setup as necessary
    #filter_setup = {"assetType": "Azure Synapse Analytics"}
    #filter_setup = {"entityType": "azure_synapse_dedicated_sql_table"}
    #filter_setup = {"collectionId":"rwk7yo"}
    #filter_setup = {"and": [{"collectionId":"rwk7yo"}, {"assetType": "Azure Data Lake Storage Gen2"}]}
    #query = client.discovery.search_entities('*', search_filter=filter_setup )
    
    
    limit = 1000 #to delete upto 1000 assets
    collection_id = "<enter value>"
    filter_setup = {"and": [{"collectionId": collection_id}, {"assetType": "Azure Data Lake Storage Gen2"}]}
    query = client.discovery.query(limit=limit, filter=filter_setup)
    
    query_list = []
    batch = []

    for entry in query["value"]:       
        query_list.append(entry["id"])

    print(query_list)
    print("Total #assets to be deleted:", len(query_list))

    start = 0
    end = len(query_list)
    batch_size = 100
    for iter in range(start, end, batch_size):
        batch = query_list[iter:iter+batch_size]
        print("Deleting:", len(batch))
        client.delete_entity(guid=batch)

    print("Done")

  
