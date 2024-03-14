# APIEntitiesBatchedBackgroundMigration

API_Entities_BatchedBackgroundMigration model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**job_class_name** | **str** |  | [optional] 
**table_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**progress** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_batched_background_migration import APIEntitiesBatchedBackgroundMigration

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBatchedBackgroundMigration from a JSON string
api_entities_batched_background_migration_instance = APIEntitiesBatchedBackgroundMigration.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBatchedBackgroundMigration.to_json())

# convert the object into a dict
api_entities_batched_background_migration_dict = api_entities_batched_background_migration_instance.to_dict()
# create an instance of APIEntitiesBatchedBackgroundMigration from a dict
api_entities_batched_background_migration_form_dict = api_entities_batched_background_migration.from_dict(api_entities_batched_background_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


