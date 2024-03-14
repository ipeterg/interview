# PostApiV4GroupsIdBadgesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_url** | **str** | URL of the badge link | 
**image_url** | **str** | URL of the badge image | 
**name** | **str** | Name for the badge | [optional] 

## Example

```python
from openapi_client.models.post_api_v4_groups_id_badges_request import PostApiV4GroupsIdBadgesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApiV4GroupsIdBadgesRequest from a JSON string
post_api_v4_groups_id_badges_request_instance = PostApiV4GroupsIdBadgesRequest.from_json(json)
# print the JSON string representation of the object
print(PostApiV4GroupsIdBadgesRequest.to_json())

# convert the object into a dict
post_api_v4_groups_id_badges_request_dict = post_api_v4_groups_id_badges_request_instance.to_dict()
# create an instance of PostApiV4GroupsIdBadgesRequest from a dict
post_api_v4_groups_id_badges_request_form_dict = post_api_v4_groups_id_badges_request.from_dict(post_api_v4_groups_id_badges_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


