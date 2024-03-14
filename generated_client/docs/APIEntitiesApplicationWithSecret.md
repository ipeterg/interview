# APIEntitiesApplicationWithSecret

API_Entities_ApplicationWithSecret model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**application_name** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**confidential** | **bool** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_application_with_secret import APIEntitiesApplicationWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesApplicationWithSecret from a JSON string
api_entities_application_with_secret_instance = APIEntitiesApplicationWithSecret.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesApplicationWithSecret.to_json())

# convert the object into a dict
api_entities_application_with_secret_dict = api_entities_application_with_secret_instance.to_dict()
# create an instance of APIEntitiesApplicationWithSecret from a dict
api_entities_application_with_secret_form_dict = api_entities_application_with_secret.from_dict(api_entities_application_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


