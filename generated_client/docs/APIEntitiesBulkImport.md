# APIEntitiesBulkImport

API_Entities_BulkImport model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_bulk_import import APIEntitiesBulkImport

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBulkImport from a JSON string
api_entities_bulk_import_instance = APIEntitiesBulkImport.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBulkImport.to_json())

# convert the object into a dict
api_entities_bulk_import_dict = api_entities_bulk_import_instance.to_dict()
# create an instance of APIEntitiesBulkImport from a dict
api_entities_bulk_import_form_dict = api_entities_bulk_import.from_dict(api_entities_bulk_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


