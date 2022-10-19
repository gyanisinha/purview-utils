from asyncio.windows_events import NULL
import json
import os
import pprint as pp
import pandas as pd

# PyApacheAtlas packages
# Connect to Atlas via a Service Principal
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient  # Communicate with your Atlas server


if __name__ == "__main__":
    """
    This script provides an example of searching modified assets based on modifiedTime and filtering those which are certified.
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

    limit = 1000
    filter_setup = {"and": [
                                {
                                    "attributeName": "modifiedTime",
                                    "operator": "gt",
                                    "attributeValue": 1002617505260
                                                            
                                }
                            ]
                    }
    #query = client.discovery.search_entities('*', search_filter=filter_setup)
    query = client.discovery.query(limit=limit, filter=filter_setup)

    query_list = []

    for entry in query["value"]:
        valid = entry.get("endorsement")
        if valid:
            if entry["endorsement"][0] == "certified":
                query_list.append(entry["qualifiedName"],)

    print("Total certified assets and recently modified:",len(query_list))
 
    print(query_list)
