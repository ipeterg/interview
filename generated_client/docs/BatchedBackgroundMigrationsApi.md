# openapi_client.BatchedBackgroundMigrationsApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v4_admin_batched_background_migrations**](BatchedBackgroundMigrationsApi.md#get_api_v4_admin_batched_background_migrations) | **GET** /api/v4/admin/batched_background_migrations | 
[**get_api_v4_admin_batched_background_migrations_id**](BatchedBackgroundMigrationsApi.md#get_api_v4_admin_batched_background_migrations_id) | **GET** /api/v4/admin/batched_background_migrations/{id} | 
[**put_api_v4_admin_batched_background_migrations_id_pause**](BatchedBackgroundMigrationsApi.md#put_api_v4_admin_batched_background_migrations_id_pause) | **PUT** /api/v4/admin/batched_background_migrations/{id}/pause | 
[**put_api_v4_admin_batched_background_migrations_id_resume**](BatchedBackgroundMigrationsApi.md#put_api_v4_admin_batched_background_migrations_id_resume) | **PUT** /api/v4/admin/batched_background_migrations/{id}/resume | 


# **get_api_v4_admin_batched_background_migrations**
> List[APIEntitiesBatchedBackgroundMigration] get_api_v4_admin_batched_background_migrations(database=database)



Get the list of batched background migrations

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_batched_background_migration import APIEntitiesBatchedBackgroundMigration
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
    api_instance = openapi_client.BatchedBackgroundMigrationsApi(api_client)
    database = 'main' # str | The name of the database, the default `main` (optional) (default to 'main')

    try:
        api_response = api_instance.get_api_v4_admin_batched_background_migrations(database=database)
        print("The response of BatchedBackgroundMigrationsApi->get_api_v4_admin_batched_background_migrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchedBackgroundMigrationsApi->get_api_v4_admin_batched_background_migrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**| The name of the database, the default &#x60;main&#x60; | [optional] [default to &#39;main&#39;]

### Return type

[**List[APIEntitiesBatchedBackgroundMigration]**](APIEntitiesBatchedBackgroundMigration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the list of batched background migrations |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_admin_batched_background_migrations_id**
> APIEntitiesBatchedBackgroundMigration get_api_v4_admin_batched_background_migrations_id(id, database=database)



Retrieve a batched background migration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_batched_background_migration import APIEntitiesBatchedBackgroundMigration
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
    api_instance = openapi_client.BatchedBackgroundMigrationsApi(api_client)
    id = 56 # int | The batched background migration id
    database = 'main' # str | The name of the database (optional) (default to 'main')

    try:
        api_response = api_instance.get_api_v4_admin_batched_background_migrations_id(id, database=database)
        print("The response of BatchedBackgroundMigrationsApi->get_api_v4_admin_batched_background_migrations_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchedBackgroundMigrationsApi->get_api_v4_admin_batched_background_migrations_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The batched background migration id | 
 **database** | **str**| The name of the database | [optional] [default to &#39;main&#39;]

### Return type

[**APIEntitiesBatchedBackgroundMigration**](APIEntitiesBatchedBackgroundMigration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a batched background migration |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_admin_batched_background_migrations_id_pause**
> APIEntitiesBatchedBackgroundMigration put_api_v4_admin_batched_background_migrations_id_pause(id, put_api_v4_admin_batched_background_migrations_id_resume_request=put_api_v4_admin_batched_background_migrations_id_resume_request)



Pause a batched background migration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_batched_background_migration import APIEntitiesBatchedBackgroundMigration
from openapi_client.models.put_api_v4_admin_batched_background_migrations_id_resume_request import PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest
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
    api_instance = openapi_client.BatchedBackgroundMigrationsApi(api_client)
    id = 56 # int | The batched background migration id
    put_api_v4_admin_batched_background_migrations_id_resume_request = openapi_client.PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest() # PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest |  (optional)

    try:
        api_response = api_instance.put_api_v4_admin_batched_background_migrations_id_pause(id, put_api_v4_admin_batched_background_migrations_id_resume_request=put_api_v4_admin_batched_background_migrations_id_resume_request)
        print("The response of BatchedBackgroundMigrationsApi->put_api_v4_admin_batched_background_migrations_id_pause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchedBackgroundMigrationsApi->put_api_v4_admin_batched_background_migrations_id_pause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The batched background migration id | 
 **put_api_v4_admin_batched_background_migrations_id_resume_request** | [**PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest**](PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest.md)|  | [optional] 

### Return type

[**APIEntitiesBatchedBackgroundMigration**](APIEntitiesBatchedBackgroundMigration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pause a batched background migration |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not found |  -  |
**422** | You can pause only &#x60;active&#x60; batched background migrations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_admin_batched_background_migrations_id_resume**
> APIEntitiesBatchedBackgroundMigration put_api_v4_admin_batched_background_migrations_id_resume(id, put_api_v4_admin_batched_background_migrations_id_resume_request=put_api_v4_admin_batched_background_migrations_id_resume_request)



Resume a batched background migration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_batched_background_migration import APIEntitiesBatchedBackgroundMigration
from openapi_client.models.put_api_v4_admin_batched_background_migrations_id_resume_request import PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest
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
    api_instance = openapi_client.BatchedBackgroundMigrationsApi(api_client)
    id = 56 # int | The batched background migration id
    put_api_v4_admin_batched_background_migrations_id_resume_request = openapi_client.PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest() # PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest |  (optional)

    try:
        api_response = api_instance.put_api_v4_admin_batched_background_migrations_id_resume(id, put_api_v4_admin_batched_background_migrations_id_resume_request=put_api_v4_admin_batched_background_migrations_id_resume_request)
        print("The response of BatchedBackgroundMigrationsApi->put_api_v4_admin_batched_background_migrations_id_resume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchedBackgroundMigrationsApi->put_api_v4_admin_batched_background_migrations_id_resume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The batched background migration id | 
 **put_api_v4_admin_batched_background_migrations_id_resume_request** | [**PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest**](PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest.md)|  | [optional] 

### Return type

[**APIEntitiesBatchedBackgroundMigration**](APIEntitiesBatchedBackgroundMigration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resume a batched background migration |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not found |  -  |
**422** | You can resume only &#x60;paused&#x60; batched background migrations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

