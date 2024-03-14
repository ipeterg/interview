# APIEntitiesBulkImports

API_Entities_BulkImports model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**bulk_import_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**source_full_path** | **str** |  | [optional] 
**destination_full_path** | **str** |  | [optional] 
**destination_name** | **str** |  | [optional] 
**destination_slug** | **str** |  | [optional] 
**destination_namespace** | **str** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**namespace_id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**failures** | [**List[APIEntitiesBulkImportsEntityFailure]**](APIEntitiesBulkImportsEntityFailure.md) |  | [optional] 
**migrate_projects** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_bulk_imports import APIEntitiesBulkImports

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBulkImports from a JSON string
api_entities_bulk_imports_instance = APIEntitiesBulkImports.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBulkImports.to_json())

# convert the object into a dict
api_entities_bulk_imports_dict = api_entities_bulk_imports_instance.to_dict()
# create an instance of APIEntitiesBulkImports from a dict
api_entities_bulk_imports_form_dict = api_entities_bulk_imports.from_dict(api_entities_bulk_imports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


