# APIEntitiesBulkImportsEntityFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | [optional] 
**step** | **str** |  | [optional] 
**exception_message** | **str** |  | [optional] 
**exception_class** | **str** |  | [optional] 
**correlation_id_value** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**pipeline_class** | **str** |  | [optional] 
**pipeline_step** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_bulk_imports_entity_failure import APIEntitiesBulkImportsEntityFailure

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBulkImportsEntityFailure from a JSON string
api_entities_bulk_imports_entity_failure_instance = APIEntitiesBulkImportsEntityFailure.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBulkImportsEntityFailure.to_json())

# convert the object into a dict
api_entities_bulk_imports_entity_failure_dict = api_entities_bulk_imports_entity_failure_instance.to_dict()
# create an instance of APIEntitiesBulkImportsEntityFailure from a dict
api_entities_bulk_imports_entity_failure_form_dict = api_entities_bulk_imports_entity_failure.from_dict(api_entities_bulk_imports_entity_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


