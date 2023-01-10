# purview-utils
## sample custom scripts using APIs/SDKs for stewardship activites


### Bulk Delete Assets (using pyapacheatlas)
[bulk_delete_assets.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_delete_assets.py)

---

### Bulk Delete Assets for a list of Fully QualifiedNames (using pyapacheatlas)
[bulk_delete_assets_fqn.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_delete_assets_fqn.py)

[list_of_assets_to_be_deleted.xlsx](https://github.com/gyanisinha/purview-utils/files/9822982/list_of_assets_to_be_deleted.xlsx)

---

### Search modified assets based on modifiedTime and filter those which are "certified" (using pyapacheatlas)
[search_modified_assets.py](https://github.com/gyanisinha/purview-utils/blob/main/search_modified_assets.py)

---

### Find ADLS assets with missing schema (using pyapacheatlas)
[find_adls_assets_with_missing_schema.py](https://github.com/gyanisinha/purview-utils/blob/main/find_adls_assets_with_missing_schema.py)

---

### Find Dedicated SQL Pool Assets (tables/views) with missing schema (using pyapacheatlas)
[find_sqldw_assets_with_missing_schema.py](https://github.com/gyanisinha/purview-utils/blob/main/find_sqldw_assets_with_missing_schema.py)

---

### Bulk update schema (if missing) for Dedicated SQL Pool Assets (tables/views)  (using pyapacheatlas)
[bulk_update_missing_schema_sqldw.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_update_missing_schema_sqldw.py)

Input template for tables: [BulkUpdateMissingSchema_table.xlsx](https://github.com/gyanisinha/purview-utils/files/10143249/BulkUpdateMissingSchema_table.xlsx)

Input template for views: [BulkUpdateMissingSchema_view.xlsx](https://github.com/gyanisinha/purview-utils/files/10143264/BulkUpdateMissingSchema_view.xlsx)

---

### Bulk create entites with schema details for Dedicated SQL Pool Assets (tables)  (using pyapacheatlas)
[bulk_create_entities_sqldw.py](https://github.com/gyanisinha/purview-utils/blob/main/bulk_create_entities_sqldw.py)

Input template for tables: [BulkUploadEntities.xlsx](https://github.com/gyanisinha/purview-utils/files/10143249/BulkUploadEntities.xlsx)
