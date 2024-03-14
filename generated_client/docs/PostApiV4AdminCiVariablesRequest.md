# PostApiV4AdminCiVariablesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the variable. Max 255 characters | 
**value** | **str** | The value of a variable | 
**protected** | **bool** | Whether the variable is protected | [optional] 
**masked** | **bool** | Whether the variable is masked | [optional] 
**raw** | **bool** | Whether the variable will be expanded | [optional] 
**variable_type** | **str** | The type of a variable. Available types are: env_var (default) and file | [optional] 

## Example

```python
from openapi_client.models.post_api_v4_admin_ci_variables_request import PostApiV4AdminCiVariablesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApiV4AdminCiVariablesRequest from a JSON string
post_api_v4_admin_ci_variables_request_instance = PostApiV4AdminCiVariablesRequest.from_json(json)
# print the JSON string representation of the object
print(PostApiV4AdminCiVariablesRequest.to_json())

# convert the object into a dict
post_api_v4_admin_ci_variables_request_dict = post_api_v4_admin_ci_variables_request_instance.to_dict()
# create an instance of PostApiV4AdminCiVariablesRequest from a dict
post_api_v4_admin_ci_variables_request_form_dict = post_api_v4_admin_ci_variables_request.from_dict(post_api_v4_admin_ci_variables_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


