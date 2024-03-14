# PostApiV4ApplicationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the application. | 
**redirect_uri** | **str** | Redirect URI of the application. | 
**scopes** | **str** | Scopes of the application. You can specify multiple scopes by separating\\                                  each scope using a space | 
**confidential** | **bool** | The application is used where the client secret can be kept confidential. Native mobile apps \\                         and Single Page Apps are considered non-confidential. Defaults to true if not supplied | [optional] [default to True]

## Example

```python
from openapi_client.models.post_api_v4_applications_request import PostApiV4ApplicationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApiV4ApplicationsRequest from a JSON string
post_api_v4_applications_request_instance = PostApiV4ApplicationsRequest.from_json(json)
# print the JSON string representation of the object
print(PostApiV4ApplicationsRequest.to_json())

# convert the object into a dict
post_api_v4_applications_request_dict = post_api_v4_applications_request_instance.to_dict()
# create an instance of PostApiV4ApplicationsRequest from a dict
post_api_v4_applications_request_form_dict = post_api_v4_applications_request.from_dict(post_api_v4_applications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


