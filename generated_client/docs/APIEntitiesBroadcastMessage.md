# APIEntitiesBroadcastMessage

API_Entities_BroadcastMessage model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**starts_at** | **str** |  | [optional] 
**ends_at** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**font** | **str** |  | [optional] 
**target_access_levels** | **str** |  | [optional] 
**target_path** | **str** |  | [optional] 
**broadcast_type** | **str** |  | [optional] 
**dismissable** | **str** |  | [optional] 
**active** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_broadcast_message import APIEntitiesBroadcastMessage

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBroadcastMessage from a JSON string
api_entities_broadcast_message_instance = APIEntitiesBroadcastMessage.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBroadcastMessage.to_json())

# convert the object into a dict
api_entities_broadcast_message_dict = api_entities_broadcast_message_instance.to_dict()
# create an instance of APIEntitiesBroadcastMessage from a dict
api_entities_broadcast_message_form_dict = api_entities_broadcast_message.from_dict(api_entities_broadcast_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


