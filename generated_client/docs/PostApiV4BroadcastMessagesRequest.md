# PostApiV4BroadcastMessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message to display | 
**starts_at** | **datetime** | Starting time | [optional] 
**ends_at** | **datetime** | Ending time | [optional] 
**color** | **str** | Background color | [optional] 
**font** | **str** | Foreground color | [optional] 
**target_access_levels** | **List[int]** | Target user roles | [optional] 
**target_path** | **str** | Target path | [optional] 
**broadcast_type** | **str** | Broadcast type. Defaults to banner | [optional] 
**dismissable** | **bool** | Is dismissable | [optional] 

## Example

```python
from openapi_client.models.post_api_v4_broadcast_messages_request import PostApiV4BroadcastMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApiV4BroadcastMessagesRequest from a JSON string
post_api_v4_broadcast_messages_request_instance = PostApiV4BroadcastMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(PostApiV4BroadcastMessagesRequest.to_json())

# convert the object into a dict
post_api_v4_broadcast_messages_request_dict = post_api_v4_broadcast_messages_request_instance.to_dict()
# create an instance of PostApiV4BroadcastMessagesRequest from a dict
post_api_v4_broadcast_messages_request_form_dict = post_api_v4_broadcast_messages_request.from_dict(post_api_v4_broadcast_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


