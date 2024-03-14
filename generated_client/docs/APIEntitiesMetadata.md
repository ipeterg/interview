# APIEntitiesMetadata

API_Entities_Metadata model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 
**kas** | [**APIEntitiesMetadataKas**](APIEntitiesMetadataKas.md) |  | [optional] 
**enterprise** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_metadata import APIEntitiesMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesMetadata from a JSON string
api_entities_metadata_instance = APIEntitiesMetadata.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesMetadata.to_json())

# convert the object into a dict
api_entities_metadata_dict = api_entities_metadata_instance.to_dict()
# create an instance of APIEntitiesMetadata from a dict
api_entities_metadata_form_dict = api_entities_metadata.from_dict(api_entities_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


