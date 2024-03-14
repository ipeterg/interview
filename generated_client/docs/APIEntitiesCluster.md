# APIEntitiesCluster

API_Entities_Cluster model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**enabled** | **str** |  | [optional] 
**managed** | **str** |  | [optional] 
**provider_type** | **str** |  | [optional] 
**platform_type** | **str** |  | [optional] 
**environment_scope** | **str** |  | [optional] 
**cluster_type** | **str** |  | [optional] 
**namespace_per_environment** | **str** |  | [optional] 
**user** | [**APIEntitiesUserBasic**](APIEntitiesUserBasic.md) |  | [optional] 
**platform_kubernetes** | [**APIEntitiesPlatformKubernetes**](APIEntitiesPlatformKubernetes.md) |  | [optional] 
**provider_gcp** | [**APIEntitiesProviderGcp**](APIEntitiesProviderGcp.md) |  | [optional] 
**management_project** | [**APIEntitiesProjectIdentity**](APIEntitiesProjectIdentity.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_cluster import APIEntitiesCluster

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesCluster from a JSON string
api_entities_cluster_instance = APIEntitiesCluster.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesCluster.to_json())

# convert the object into a dict
api_entities_cluster_dict = api_entities_cluster_instance.to_dict()
# create an instance of APIEntitiesCluster from a dict
api_entities_cluster_form_dict = api_entities_cluster.from_dict(api_entities_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


