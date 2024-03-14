# APIEntitiesAccessRequester

API_Entities_AccessRequester model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**avatar_path** | **str** |  | [optional] 
**custom_attributes** | [**List[APIEntitiesCustomAttribute]**](APIEntitiesCustomAttribute.md) |  | [optional] 
**web_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**requested_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_access_requester import APIEntitiesAccessRequester

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesAccessRequester from a JSON string
api_entities_access_requester_instance = APIEntitiesAccessRequester.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesAccessRequester.to_json())

# convert the object into a dict
api_entities_access_requester_dict = api_entities_access_requester_instance.to_dict()
# create an instance of APIEntitiesAccessRequester from a dict
api_entities_access_requester_form_dict = api_entities_access_requester.from_dict(api_entities_access_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


