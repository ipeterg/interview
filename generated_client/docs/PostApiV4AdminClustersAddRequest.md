# PostApiV4AdminClustersAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Cluster name | 
**enabled** | **bool** | Determines if cluster is active or not, defaults to true | [optional] [default to True]
**environment_scope** | **str** | The associated environment to the cluster | [optional] [default to '*']
**namespace_per_environment** | **bool** | Deploy each environment to a separate Kubernetes namespace | [optional] [default to True]
**domain** | **str** | Cluster base domain | [optional] 
**management_project_id** | **int** | The ID of the management project | [optional] 
**managed** | **bool** | Determines if GitLab will manage namespaces and service accounts for this cluster, defaults to true | [optional] [default to True]
**platform_kubernetes_attributes_api_url** | **str** | URL to access the Kubernetes API | 
**platform_kubernetes_attributes_token** | **str** | Token to authenticate against Kubernetes | 
**platform_kubernetes_attributes_ca_cert** | **str** | TLS certificate (needed if API is using a self-signed TLS certificate) | [optional] 
**platform_kubernetes_attributes_namespace** | **str** | Unique namespace related to Project | [optional] 
**platform_kubernetes_attributes_authorization_type** | **str** | Cluster authorization type, defaults to RBAC | [optional] [default to 'rbac']

## Example

```python
from openapi_client.models.post_api_v4_admin_clusters_add_request import PostApiV4AdminClustersAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApiV4AdminClustersAddRequest from a JSON string
post_api_v4_admin_clusters_add_request_instance = PostApiV4AdminClustersAddRequest.from_json(json)
# print the JSON string representation of the object
print(PostApiV4AdminClustersAddRequest.to_json())

# convert the object into a dict
post_api_v4_admin_clusters_add_request_dict = post_api_v4_admin_clusters_add_request_instance.to_dict()
# create an instance of PostApiV4AdminClustersAddRequest from a dict
post_api_v4_admin_clusters_add_request_form_dict = post_api_v4_admin_clusters_add_request.from_dict(post_api_v4_admin_clusters_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


