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


    #filter_setup = {"assetType": "Azure Synapse Analytics"}
    #filter_setup = {"entityType": "azure_synapse_dedicated_sql_table"}
    #filter_setup = {"collectionId":"rwk7yo"}
    filter_setup = {"and": [{"collectionId":"rwk7yo"}, {"assetType": "Azure Data Lake Storage Gen2"}]}
    query = client.discovery.search_entities('*', search_filter=filter_setup )
    
    batch = []

    for entry in query:       
            batch.append(entry["id"])
            if len(batch) == 1000:
                #uncomment delete after you have tested the output using print(batch)
                #client.delete_entity(guid=batch)
                batch = []
        
            # Out of loop, clean up batches
            if len(batch) > 0:
                #uncomment delete after you have tested the output using print(batch)
                #client.delete_entity(guid=batch)
                print("Done")

    print(batch)  
    print(len(batch))

  
