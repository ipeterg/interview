# openapi_client.ClustersApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_admin_clusters_cluster_id**](ClustersApi.md#delete_api_v4_admin_clusters_cluster_id) | **DELETE** /api/v4/admin/clusters/{cluster_id} | Delete instance cluster
[**get_api_v4_admin_clusters**](ClustersApi.md#get_api_v4_admin_clusters) | **GET** /api/v4/admin/clusters | List instance clusters
[**get_api_v4_admin_clusters_cluster_id**](ClustersApi.md#get_api_v4_admin_clusters_cluster_id) | **GET** /api/v4/admin/clusters/{cluster_id} | Get a single instance cluster
[**post_api_v4_admin_clusters_add**](ClustersApi.md#post_api_v4_admin_clusters_add) | **POST** /api/v4/admin/clusters/add | Add existing instance cluster
[**put_api_v4_admin_clusters_cluster_id**](ClustersApi.md#put_api_v4_admin_clusters_cluster_id) | **PUT** /api/v4/admin/clusters/{cluster_id} | Edit instance cluster


# **delete_api_v4_admin_clusters_cluster_id**
> APIEntitiesCluster delete_api_v4_admin_clusters_cluster_id(cluster_id)

Delete instance cluster

This feature was introduced in GitLab 13.2. Deletes an existing instance cluster. Does not remove existing resources within the connected Kubernetes cluster.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_cluster import APIEntitiesCluster
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.gitlab.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.gitlab.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClustersApi(api_client)
    cluster_id = 56 # int | The cluster ID

    try:
        # Delete instance cluster
        api_response = api_instance.delete_api_v4_admin_clusters_cluster_id(cluster_id)
        print("The response of ClustersApi->delete_api_v4_admin_clusters_cluster_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_api_v4_admin_clusters_cluster_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| The cluster ID | 

### Return type

[**APIEntitiesCluster**](APIEntitiesCluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Delete instance cluster |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_admin_clusters**
> List[APIEntitiesCluster] get_api_v4_admin_clusters()

List instance clusters

This feature was introduced in GitLab 13.2. Returns a list of instance clusters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_cluster import APIEntitiesCluster
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.gitlab.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.gitlab.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClustersApi(api_client)

    try:
        # List instance clusters
        api_response = api_instance.get_api_v4_admin_clusters()
        print("The response of ClustersApi->get_api_v4_admin_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_api_v4_admin_clusters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[APIEntitiesCluster]**](APIEntitiesCluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List instance clusters |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_admin_clusters_cluster_id**
> APIEntitiesCluster get_api_v4_admin_clusters_cluster_id(cluster_id)

Get a single instance cluster

This feature was introduced in GitLab 13.2. Returns a single instance cluster.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_cluster import APIEntitiesCluster
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.gitlab.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.gitlab.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClustersApi(api_client)
    cluster_id = 56 # int | The cluster ID

    try:
        # Get a single instance cluster
        api_response = api_instance.get_api_v4_admin_clusters_cluster_id(cluster_id)
        print("The response of ClustersApi->get_api_v4_admin_clusters_cluster_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_api_v4_admin_clusters_cluster_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| The cluster ID | 

### Return type

[**APIEntitiesCluster**](APIEntitiesCluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a single instance cluster |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_admin_clusters_add**
> APIEntitiesCluster post_api_v4_admin_clusters_add(post_api_v4_admin_clusters_add_request)

Add existing instance cluster

This feature was introduced in GitLab 13.2. Adds an existing Kubernetes instance cluster.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_cluster import APIEntitiesCluster
from openapi_client.models.post_api_v4_admin_clusters_add_request import PostApiV4AdminClustersAddRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.gitlab.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.gitlab.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClustersApi(api_client)
    post_api_v4_admin_clusters_add_request = openapi_client.PostApiV4AdminClustersAddRequest() # PostApiV4AdminClustersAddRequest | 

    try:
        # Add existing instance cluster
        api_response = api_instance.post_api_v4_admin_clusters_add(post_api_v4_admin_clusters_add_request)
        print("The response of ClustersApi->post_api_v4_admin_clusters_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->post_api_v4_admin_clusters_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_api_v4_admin_clusters_add_request** | [**PostApiV4AdminClustersAddRequest**](PostApiV4AdminClustersAddRequest.md)|  | 

### Return type

[**APIEntitiesCluster**](APIEntitiesCluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Add existing instance cluster |  -  |
**400** | Validation error |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_admin_clusters_cluster_id**
> APIEntitiesCluster put_api_v4_admin_clusters_cluster_id(cluster_id, put_api_v4_admin_clusters_cluster_id_request=put_api_v4_admin_clusters_cluster_id_request)

Edit instance cluster

This feature was introduced in GitLab 13.2. Updates an existing instance cluster.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_cluster import APIEntitiesCluster
from openapi_client.models.put_api_v4_admin_clusters_cluster_id_request import PutApiV4AdminClustersClusterIdRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.gitlab.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.gitlab.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClustersApi(api_client)
    cluster_id = 56 # int | The cluster ID
    put_api_v4_admin_clusters_cluster_id_request = openapi_client.PutApiV4AdminClustersClusterIdRequest() # PutApiV4AdminClustersClusterIdRequest |  (optional)

    try:
        # Edit instance cluster
        api_response = api_instance.put_api_v4_admin_clusters_cluster_id(cluster_id, put_api_v4_admin_clusters_cluster_id_request=put_api_v4_admin_clusters_cluster_id_request)
        print("The response of ClustersApi->put_api_v4_admin_clusters_cluster_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->put_api_v4_admin_clusters_cluster_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| The cluster ID | 
 **put_api_v4_admin_clusters_cluster_id_request** | [**PutApiV4AdminClustersClusterIdRequest**](PutApiV4AdminClustersClusterIdRequest.md)|  | [optional] 

### Return type

[**APIEntitiesCluster**](APIEntitiesCluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit instance cluster |  -  |
**400** | Validation error |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

