# PutApiV4AdminCiVariablesKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of a variable | [optional] 
**protected** | **bool** | Whether the variable is protected | [optional] 
**masked** | **bool** | Whether the variable is masked | [optional] 
**raw** | **bool** | Whether the variable will be expanded | [optional] 
**variable_type** | **str** | The type of a variable. Available types are: env_var (default) and file | [optional] 

## Example

```python
from openapi_client.models.put_api_v4_admin_ci_variables_key_request import PutApiV4AdminCiVariablesKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutApiV4AdminCiVariablesKeyRequest from a JSON string
put_api_v4_admin_ci_variables_key_request_instance = PutApiV4AdminCiVariablesKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PutApiV4AdminCiVariablesKeyRequest.to_json())

# convert the object into a dict
put_api_v4_admin_ci_variables_key_request_dict = put_api_v4_admin_ci_variables_key_request_instance.to_dict()
# create an instance of PutApiV4AdminCiVariablesKeyRequest from a dict
put_api_v4_admin_ci_variables_key_request_form_dict = put_api_v4_admin_ci_variables_key_request.from_dict(put_api_v4_admin_ci_variables_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


