# PutApiV4GroupsIdAccessRequestsUserIdApproveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **int** | A valid access level (defaults: &#x60;30&#x60;, the Developer role) | [optional] [default to 30]

## Example

```python
from openapi_client.models.put_api_v4_groups_id_access_requests_user_id_approve_request import PutApiV4GroupsIdAccessRequestsUserIdApproveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutApiV4GroupsIdAccessRequestsUserIdApproveRequest from a JSON string
put_api_v4_groups_id_access_requests_user_id_approve_request_instance = PutApiV4GroupsIdAccessRequestsUserIdApproveRequest.from_json(json)
# print the JSON string representation of the object
print(PutApiV4GroupsIdAccessRequestsUserIdApproveRequest.to_json())

# convert the object into a dict
put_api_v4_groups_id_access_requests_user_id_approve_request_dict = put_api_v4_groups_id_access_requests_user_id_approve_request_instance.to_dict()
# create an instance of PutApiV4GroupsIdAccessRequestsUserIdApproveRequest from a dict
put_api_v4_groups_id_access_requests_user_id_approve_request_form_dict = put_api_v4_groups_id_access_requests_user_id_approve_request.from_dict(put_api_v4_groups_id_access_requests_user_id_approve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


