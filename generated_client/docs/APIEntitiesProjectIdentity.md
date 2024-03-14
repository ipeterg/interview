# APIEntitiesProjectIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_with_namespace** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**path_with_namespace** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_project_identity import APIEntitiesProjectIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesProjectIdentity from a JSON string
api_entities_project_identity_instance = APIEntitiesProjectIdentity.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesProjectIdentity.to_json())

# convert the object into a dict
api_entities_project_identity_dict = api_entities_project_identity_instance.to_dict()
# create an instance of APIEntitiesProjectIdentity from a dict
api_entities_project_identity_form_dict = api_entities_project_identity.from_dict(api_entities_project_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


