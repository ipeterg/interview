# PutApiV4AdminClustersClusterIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Cluster name | [optional] 
**enabled** | **bool** | Enable or disable Gitlab&#39;s connection to your Kubernetes cluster | [optional] 
**environment_scope** | **str** | The associated environment to the cluster | [optional] 
**namespace_per_environment** | **bool** | Deploy each environment to a separate Kubernetes namespace | [optional] [default to True]
**domain** | **str** | Cluster base domain | [optional] 
**management_project_id** | **int** | The ID of the management project | [optional] 
**managed** | **bool** | Determines if GitLab will manage namespaces and service accounts for this cluster | [optional] 
**platform_kubernetes_attributes_api_url** | **str** | URL to access the Kubernetes API | [optional] 
**platform_kubernetes_attributes_token** | **str** | Token to authenticate against Kubernetes | [optional] 
**platform_kubernetes_attributes_ca_cert** | **str** | TLS certificate (needed if API is using a self-signed TLS certificate) | [optional] 
**platform_kubernetes_attributes_namespace** | **str** | Unique namespace related to Project | [optional] 

## Example

```python
from openapi_client.models.put_api_v4_admin_clusters_cluster_id_request import PutApiV4AdminClustersClusterIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutApiV4AdminClustersClusterIdRequest from a JSON string
put_api_v4_admin_clusters_cluster_id_request_instance = PutApiV4AdminClustersClusterIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutApiV4AdminClustersClusterIdRequest.to_json())

# convert the object into a dict
put_api_v4_admin_clusters_cluster_id_request_dict = put_api_v4_admin_clusters_cluster_id_request_instance.to_dict()
# create an instance of PutApiV4AdminClustersClusterIdRequest from a dict
put_api_v4_admin_clusters_cluster_id_request_form_dict = put_api_v4_admin_clusters_cluster_id_request.from_dict(put_api_v4_admin_clusters_cluster_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


