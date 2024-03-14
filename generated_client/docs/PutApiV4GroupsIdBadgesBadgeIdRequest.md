# PutApiV4GroupsIdBadgesBadgeIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_url** | **str** | URL of the badge link | [optional] 
**image_url** | **str** | URL of the badge image | [optional] 
**name** | **str** | Name for the badge | [optional] 

## Example

```python
from openapi_client.models.put_api_v4_groups_id_badges_badge_id_request import PutApiV4GroupsIdBadgesBadgeIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutApiV4GroupsIdBadgesBadgeIdRequest from a JSON string
put_api_v4_groups_id_badges_badge_id_request_instance = PutApiV4GroupsIdBadgesBadgeIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutApiV4GroupsIdBadgesBadgeIdRequest.to_json())

# convert the object into a dict
put_api_v4_groups_id_badges_badge_id_request_dict = put_api_v4_groups_id_badges_badge_id_request_instance.to_dict()
# create an instance of PutApiV4GroupsIdBadgesBadgeIdRequest from a dict
put_api_v4_groups_id_badges_badge_id_request_form_dict = put_api_v4_groups_id_badges_badge_id_request.from_dict(put_api_v4_groups_id_badges_badge_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


