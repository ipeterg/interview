# APIEntitiesBranch

API_Entities_Branch model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**commit** | [**APIEntitiesCommit**](APIEntitiesCommit.md) |  | [optional] 
**merged** | **bool** |  | [optional] 
**protected** | **bool** |  | [optional] 
**developers_can_push** | **bool** |  | [optional] 
**developers_can_merge** | **bool** |  | [optional] 
**can_push** | **bool** |  | [optional] 
**default** | **bool** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_branch import APIEntitiesBranch

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBranch from a JSON string
api_entities_branch_instance = APIEntitiesBranch.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBranch.to_json())

# convert the object into a dict
api_entities_branch_dict = api_entities_branch_instance.to_dict()
# create an instance of APIEntitiesBranch from a dict
api_entities_branch_form_dict = api_entities_branch.from_dict(api_entities_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


