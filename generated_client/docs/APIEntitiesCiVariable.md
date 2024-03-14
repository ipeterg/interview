# APIEntitiesCiVariable

API_Entities_Ci_Variable model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 
**masked** | **bool** |  | [optional] 
**raw** | **bool** |  | [optional] 
**environment_scope** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_ci_variable import APIEntitiesCiVariable

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesCiVariable from a JSON string
api_entities_ci_variable_instance = APIEntitiesCiVariable.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesCiVariable.to_json())

# convert the object into a dict
api_entities_ci_variable_dict = api_entities_ci_variable_instance.to_dict()
# create an instance of APIEntitiesCiVariable from a dict
api_entities_ci_variable_form_dict = api_entities_ci_variable.from_dict(api_entities_ci_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


