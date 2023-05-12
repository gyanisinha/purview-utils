# purview-utils

#### Pre-reqs: 

- Read about PyApacheAtlas: https://datasmackdown.com/oss/pyapacheatlas/
- Install https://pypi.org/project/pyapacheatlas/
- Create service principal: https://learn.microsoft.com/en-us/azure/purview/create-service-principal-azure


## Sample codes using Microsoft Purview REST APIs/SDKs for stewardship activites


### Create custom process (using pyapacheatlas)
[custom_process.py](https://github.com/gyanisinha/purview-utils/blob/main/custom_process.py)

use input template for custom process: [custom_process.xlsx](https://github.com/gyanisinha/purview-utils/files/11463440/custom_process.xlsx)


---

### Bulk update column level lineage with custom process (created above) for existing assets (using pyapacheatlas)
[custom_process_column_lineage.py](https://github.com/gyanisinha/purview-utils/blob/main/custom_process_column_lineage.py)

use input template for columnMapping: [custom_process_column_lineage.xlsx](https://github.com/gyanisinha/purview-utils/files/11463400/custom_process_column_lineage.xlsx)


---

### Bulk delete assets (using pyapacheatlas)
[bulk_delete_assets.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_delete_assets.py)


---

### Bulk delete assets for a list of Fully QualifiedNames (using pyapacheatlas)
[bulk_delete_assets_fqn.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_delete_assets_fqn.py)

[list_of_assets_to_be_deleted.xlsx](https://github.com/gyanisinha/purview-utils/files/9822982/list_of_assets_to_be_deleted.xlsx)

---

### Search modified assets based on modifiedTime and filter those which are "certified" (using pyapacheatlas)
[search_modified_assets.py](https://github.com/gyanisinha/purview-utils/blob/main/search_modified_assets.py)

---

### Find ADLS assets with missing schema (using pyapacheatlas)
[find_adls_assets_with_missing_schema.py](https://github.com/gyanisinha/purview-utils/blob/main/find_adls_assets_with_missing_schema.py)

---

### Find Dedicated SQL Pool assets (tables/views) with missing schema (using pyapacheatlas)
[find_sqldw_assets_with_missing_schema.py](https://github.com/gyanisinha/purview-utils/blob/main/find_sqldw_assets_with_missing_schema.py)

---

### Bulk update schema (if missing) for Dedicated SQL Pool assets (tables/views)  (using pyapacheatlas)

[bulk_update_missing_schema_sqldw.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_update_missing_schema_sqldw.py)

Input template for tables: [BulkUpdateMissingSchema_table.xlsx](https://github.com/gyanisinha/purview-utils/files/10143249/BulkUpdateMissingSchema_table.xlsx)

Input template for views: [BulkUpdateMissingSchema_view.xlsx](https://github.com/gyanisinha/purview-utils/files/10143264/BulkUpdateMissingSchema_view.xlsx)

---

### Bulk create entities with schema details for Dedicated SQL Pool assets (tables)  (using pyapacheatlas)
[bulk_create_entities_sqldw.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_create_entities_sqldw.py)

Input template for tables: [BulkUploadEntities.xlsx](https://github.com/gyanisinha/purview-utils/files/10383537/BulkUploadEntities.xlsx)


---


### Move entities to another collection (using pyapacheatlas)
[bulk_move_entities_collection.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_move_entities_collection.py)

---

# Disclaimer

Sample Code Disclaimer: This Sample Code is provided for the purpose of illustration only and is not intended to be used in a production environment. THIS SAMPLE CODE AND ANY RELATED INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. 
