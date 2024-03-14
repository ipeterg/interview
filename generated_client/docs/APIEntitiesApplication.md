# APIEntitiesApplication

API_Entities_Application model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**application_name** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**confidential** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_application import APIEntitiesApplication

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesApplication from a JSON string
api_entities_application_instance = APIEntitiesApplication.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesApplication.to_json())

# convert the object into a dict
api_entities_application_dict = api_entities_application_instance.to_dict()
# create an instance of APIEntitiesApplication from a dict
api_entities_application_form_dict = api_entities_application.from_dict(api_entities_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


