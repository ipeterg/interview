# APIEntitiesBasicBadgeDetails

API_Entities_BasicBadgeDetails model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**link_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**rendered_link_url** | **str** |  | [optional] 
**rendered_image_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_basic_badge_details import APIEntitiesBasicBadgeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBasicBadgeDetails from a JSON string
api_entities_basic_badge_details_instance = APIEntitiesBasicBadgeDetails.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBasicBadgeDetails.to_json())

# convert the object into a dict
api_entities_basic_badge_details_dict = api_entities_basic_badge_details_instance.to_dict()
# create an instance of APIEntitiesBasicBadgeDetails from a dict
api_entities_basic_badge_details_form_dict = api_entities_basic_badge_details.from_dict(api_entities_basic_badge_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


