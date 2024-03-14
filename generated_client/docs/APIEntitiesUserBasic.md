# APIEntitiesUserBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**avatar_path** | **str** |  | [optional] 
**custom_attributes** | [**List[APIEntitiesCustomAttribute]**](APIEntitiesCustomAttribute.md) |  | [optional] 
**web_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_user_basic import APIEntitiesUserBasic

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesUserBasic from a JSON string
api_entities_user_basic_instance = APIEntitiesUserBasic.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesUserBasic.to_json())

# convert the object into a dict
api_entities_user_basic_dict = api_entities_user_basic_instance.to_dict()
# create an instance of APIEntitiesUserBasic from a dict
api_entities_user_basic_form_dict = api_entities_user_basic.from_dict(api_entities_user_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


