# APIEntitiesBadge

API_Entities_Badge model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**link_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**rendered_link_url** | **str** |  | [optional] 
**rendered_image_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_badge import APIEntitiesBadge

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesBadge from a JSON string
api_entities_badge_instance = APIEntitiesBadge.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesBadge.to_json())

# convert the object into a dict
api_entities_badge_dict = api_entities_badge_instance.to_dict()
# create an instance of APIEntitiesBadge from a dict
api_entities_badge_form_dict = api_entities_badge.from_dict(api_entities_badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


