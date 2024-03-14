# APIEntitiesAppearance

API_Entities_Appearance model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**pwa_name** | **str** |  | [optional] 
**pwa_short_name** | **str** |  | [optional] 
**pwa_description** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**pwa_icon** | **str** |  | [optional] 
**header_logo** | **str** |  | [optional] 
**favicon** | **str** |  | [optional] 
**new_project_guidelines** | **str** |  | [optional] 
**profile_image_guidelines** | **str** |  | [optional] 
**header_message** | **str** |  | [optional] 
**footer_message** | **str** |  | [optional] 
**message_background_color** | **str** |  | [optional] 
**message_font_color** | **str** |  | [optional] 
**email_header_and_footer_enabled** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_appearance import APIEntitiesAppearance

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesAppearance from a JSON string
api_entities_appearance_instance = APIEntitiesAppearance.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesAppearance.to_json())

# convert the object into a dict
api_entities_appearance_dict = api_entities_appearance_instance.to_dict()
# create an instance of APIEntitiesAppearance from a dict
api_entities_appearance_form_dict = api_entities_appearance.from_dict(api_entities_appearance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


