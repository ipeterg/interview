# openapi_client.BulkImportsApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v4_bulk_imports**](BulkImportsApi.md#get_api_v4_bulk_imports) | **GET** /api/v4/bulk_imports | List all GitLab Migrations
[**get_api_v4_bulk_imports_entities**](BulkImportsApi.md#get_api_v4_bulk_imports_entities) | **GET** /api/v4/bulk_imports/entities | List all GitLab Migrations&#39; entities
[**get_api_v4_bulk_imports_import_id**](BulkImportsApi.md#get_api_v4_bulk_imports_import_id) | **GET** /api/v4/bulk_imports/{import_id} | Get GitLab Migration details
[**get_api_v4_bulk_imports_import_id_entities**](BulkImportsApi.md#get_api_v4_bulk_imports_import_id_entities) | **GET** /api/v4/bulk_imports/{import_id}/entities | List GitLab Migration entities
[**get_api_v4_bulk_imports_import_id_entities_entity_id**](BulkImportsApi.md#get_api_v4_bulk_imports_import_id_entities_entity_id) | **GET** /api/v4/bulk_imports/{import_id}/entities/{entity_id} | Get GitLab Migration entity details
[**post_api_v4_bulk_imports**](BulkImportsApi.md#post_api_v4_bulk_imports) | **POST** /api/v4/bulk_imports | Start a new GitLab Migration


# **get_api_v4_bulk_imports**
> List[APIEntitiesBulkImport] get_api_v4_bulk_imports(page=page, per_page=per_page, sort=sort, status=status)

List all GitLab Migrations

This feature was introduced in GitLab 14.1.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_bulk_import import APIEntitiesBulkImport
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
    api_instance = openapi_client.BulkImportsApi(api_client)
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)
    sort = 'desc' # str | Return GitLab Migrations sorted in created by `asc` or `desc` order. (optional) (default to 'desc')
    status = 'status_example' # str | Return GitLab Migrations with specified status (optional)

    try:
        # List all GitLab Migrations
        api_response = api_instance.get_api_v4_bulk_imports(page=page, per_page=per_page, sort=sort, status=status)
        print("The response of BulkImportsApi->get_api_v4_bulk_imports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportsApi->get_api_v4_bulk_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]
 **sort** | **str**| Return GitLab Migrations sorted in created by &#x60;asc&#x60; or &#x60;desc&#x60; order. | [optional] [default to &#39;desc&#39;]
 **status** | **str**| Return GitLab Migrations with specified status | [optional] 

### Return type

[**List[APIEntitiesBulkImport]**](APIEntitiesBulkImport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all GitLab Migrations |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_bulk_imports_entities**
> List[APIEntitiesBulkImports] get_api_v4_bulk_imports_entities(page=page, per_page=per_page, sort=sort, status=status)

List all GitLab Migrations' entities

This feature was introduced in GitLab 14.1.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_bulk_imports import APIEntitiesBulkImports
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
    api_instance = openapi_client.BulkImportsApi(api_client)
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)
    sort = 'desc' # str | Return GitLab Migrations sorted in created by `asc` or `desc` order. (optional) (default to 'desc')
    status = 'status_example' # str | Return all GitLab Migrations' entities with specified status (optional)

    try:
        # List all GitLab Migrations' entities
        api_response = api_instance.get_api_v4_bulk_imports_entities(page=page, per_page=per_page, sort=sort, status=status)
        print("The response of BulkImportsApi->get_api_v4_bulk_imports_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportsApi->get_api_v4_bulk_imports_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]
 **sort** | **str**| Return GitLab Migrations sorted in created by &#x60;asc&#x60; or &#x60;desc&#x60; order. | [optional] [default to &#39;desc&#39;]
 **status** | **str**| Return all GitLab Migrations&#39; entities with specified status | [optional] 

### Return type

[**List[APIEntitiesBulkImports]**](APIEntitiesBulkImports.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all GitLab Migrations&#39; entities |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_bulk_imports_import_id**
> APIEntitiesBulkImport get_api_v4_bulk_imports_import_id(import_id)

Get GitLab Migration details

This feature was introduced in GitLab 14.1.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_bulk_import import APIEntitiesBulkImport
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
    api_instance = openapi_client.BulkImportsApi(api_client)
    import_id = 56 # int | The ID of user's GitLab Migration

    try:
        # Get GitLab Migration details
        api_response = api_instance.get_api_v4_bulk_imports_import_id(import_id)
        print("The response of BulkImportsApi->get_api_v4_bulk_imports_import_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportsApi->get_api_v4_bulk_imports_import_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **int**| The ID of user&#39;s GitLab Migration | 

### Return type

[**APIEntitiesBulkImport**](APIEntitiesBulkImport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get GitLab Migration details |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_bulk_imports_import_id_entities**
> List[APIEntitiesBulkImports] get_api_v4_bulk_imports_import_id_entities(import_id, status=status, page=page, per_page=per_page)

List GitLab Migration entities

This feature was introduced in GitLab 14.1.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_bulk_imports import APIEntitiesBulkImports
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
    api_instance = openapi_client.BulkImportsApi(api_client)
    import_id = 56 # int | The ID of user's GitLab Migration
    status = 'status_example' # str | Return import entities with specified status (optional)
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)

    try:
        # List GitLab Migration entities
        api_response = api_instance.get_api_v4_bulk_imports_import_id_entities(import_id, status=status, page=page, per_page=per_page)
        print("The response of BulkImportsApi->get_api_v4_bulk_imports_import_id_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportsApi->get_api_v4_bulk_imports_import_id_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **int**| The ID of user&#39;s GitLab Migration | 
 **status** | **str**| Return import entities with specified status | [optional] 
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]

### Return type

[**List[APIEntitiesBulkImports]**](APIEntitiesBulkImports.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List GitLab Migration entities |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_bulk_imports_import_id_entities_entity_id**
> APIEntitiesBulkImports get_api_v4_bulk_imports_import_id_entities_entity_id(import_id, entity_id)

Get GitLab Migration entity details

This feature was introduced in GitLab 14.1.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_bulk_imports import APIEntitiesBulkImports
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
    api_instance = openapi_client.BulkImportsApi(api_client)
    import_id = 56 # int | The ID of user's GitLab Migration
    entity_id = 56 # int | The ID of GitLab Migration entity

    try:
        # Get GitLab Migration entity details
        api_response = api_instance.get_api_v4_bulk_imports_import_id_entities_entity_id(import_id, entity_id)
        print("The response of BulkImportsApi->get_api_v4_bulk_imports_import_id_entities_entity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportsApi->get_api_v4_bulk_imports_import_id_entities_entity_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **int**| The ID of user&#39;s GitLab Migration | 
 **entity_id** | **int**| The ID of GitLab Migration entity | 

### Return type

[**APIEntitiesBulkImports**](APIEntitiesBulkImports.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get GitLab Migration entity details |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_bulk_imports**
> APIEntitiesBulkImport post_api_v4_bulk_imports(configuration_url, configuration_access_token, entities_source_type, entities_source_full_path, entities_destination_namespace, entities_destination_slug=entities_destination_slug, entities_destination_name=entities_destination_name, entities_migrate_projects=entities_migrate_projects)

Start a new GitLab Migration

This feature was introduced in GitLab 14.2.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_bulk_import import APIEntitiesBulkImport
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
    api_instance = openapi_client.BulkImportsApi(api_client)
    configuration_url = 'configuration_url_example' # str | Source GitLab instance URL
    configuration_access_token = 'configuration_access_token_example' # str | Access token to the source GitLab instance
    entities_source_type = ['entities_source_type_example'] # List[str] | Source entity type
    entities_source_full_path = ['entities_source_full_path_example'] # List[str] | Relative path of the source entity to import
    entities_destination_namespace = ['entities_destination_namespace_example'] # List[str] | Destination namespace for the entity
    entities_destination_slug = ['entities_destination_slug_example'] # List[str] | Destination slug for the entity (optional)
    entities_destination_name = ['entities_destination_name_example'] # List[str] | Deprecated: Use :destination_slug instead. Destination slug for the entity (optional)
    entities_migrate_projects = [True] # List[bool] | Indicates group migration should include nested projects (optional)

    try:
        # Start a new GitLab Migration
        api_response = api_instance.post_api_v4_bulk_imports(configuration_url, configuration_access_token, entities_source_type, entities_source_full_path, entities_destination_namespace, entities_destination_slug=entities_destination_slug, entities_destination_name=entities_destination_name, entities_migrate_projects=entities_migrate_projects)
        print("The response of BulkImportsApi->post_api_v4_bulk_imports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportsApi->post_api_v4_bulk_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_url** | **str**| Source GitLab instance URL | 
 **configuration_access_token** | **str**| Access token to the source GitLab instance | 
 **entities_source_type** | [**List[str]**](str.md)| Source entity type | 
 **entities_source_full_path** | [**List[str]**](str.md)| Relative path of the source entity to import | 
 **entities_destination_namespace** | [**List[str]**](str.md)| Destination namespace for the entity | 
 **entities_destination_slug** | [**List[str]**](str.md)| Destination slug for the entity | [optional] 
 **entities_destination_name** | [**List[str]**](str.md)| Deprecated: Use :destination_slug instead. Destination slug for the entity | [optional] 
 **entities_migrate_projects** | [**List[bool]**](bool.md)| Indicates group migration should include nested projects | [optional] 

### Return type

[**APIEntitiesBulkImport**](APIEntitiesBulkImport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Start a new GitLab Migration |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Unprocessable entity |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

