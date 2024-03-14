# APIEntitiesProviderGcp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**status_name** | **str** |  | [optional] 
**gcp_project_id** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 
**machine_type** | **str** |  | [optional] 
**num_nodes** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_provider_gcp import APIEntitiesProviderGcp

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesProviderGcp from a JSON string
api_entities_provider_gcp_instance = APIEntitiesProviderGcp.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesProviderGcp.to_json())

# convert the object into a dict
api_entities_provider_gcp_dict = api_entities_provider_gcp_instance.to_dict()
# create an instance of APIEntitiesProviderGcp from a dict
api_entities_provider_gcp_form_dict = api_entities_provider_gcp.from_dict(api_entities_provider_gcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


