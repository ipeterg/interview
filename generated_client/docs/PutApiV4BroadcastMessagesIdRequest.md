# PutApiV4BroadcastMessagesIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message to display | [optional] 
**starts_at** | **datetime** | Starting time | [optional] 
**ends_at** | **datetime** | Ending time | [optional] 
**color** | **str** | Background color | [optional] 
**font** | **str** | Foreground color | [optional] 
**target_access_levels** | **List[int]** | Target user roles | [optional] 
**target_path** | **str** | Target path | [optional] 
**broadcast_type** | **str** | Broadcast Type | [optional] 
**dismissable** | **bool** | Is dismissable | [optional] 

## Example

```python
from openapi_client.models.put_api_v4_broadcast_messages_id_request import PutApiV4BroadcastMessagesIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutApiV4BroadcastMessagesIdRequest from a JSON string
put_api_v4_broadcast_messages_id_request_instance = PutApiV4BroadcastMessagesIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutApiV4BroadcastMessagesIdRequest.to_json())

# convert the object into a dict
put_api_v4_broadcast_messages_id_request_dict = put_api_v4_broadcast_messages_id_request_instance.to_dict()
# create an instance of PutApiV4BroadcastMessagesIdRequest from a dict
put_api_v4_broadcast_messages_id_request_form_dict = put_api_v4_broadcast_messages_id_request.from_dict(put_api_v4_broadcast_messages_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


