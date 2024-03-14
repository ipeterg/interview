# APIEntitiesPlatformKubernetes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**authorization_type** | **str** |  | [optional] 
**ca_cert** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_platform_kubernetes import APIEntitiesPlatformKubernetes

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesPlatformKubernetes from a JSON string
api_entities_platform_kubernetes_instance = APIEntitiesPlatformKubernetes.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesPlatformKubernetes.to_json())

# convert the object into a dict
api_entities_platform_kubernetes_dict = api_entities_platform_kubernetes_instance.to_dict()
# create an instance of APIEntitiesPlatformKubernetes from a dict
api_entities_platform_kubernetes_form_dict = api_entities_platform_kubernetes.from_dict(api_entities_platform_kubernetes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


