# openapi_client.CiVariablesApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_admin_ci_variables_key**](CiVariablesApi.md#delete_api_v4_admin_ci_variables_key) | **DELETE** /api/v4/admin/ci/variables/{key} | 
[**get_api_v4_admin_ci_variables**](CiVariablesApi.md#get_api_v4_admin_ci_variables) | **GET** /api/v4/admin/ci/variables | 
[**get_api_v4_admin_ci_variables_key**](CiVariablesApi.md#get_api_v4_admin_ci_variables_key) | **GET** /api/v4/admin/ci/variables/{key} | 
[**post_api_v4_admin_ci_variables**](CiVariablesApi.md#post_api_v4_admin_ci_variables) | **POST** /api/v4/admin/ci/variables | 
[**put_api_v4_admin_ci_variables_key**](CiVariablesApi.md#put_api_v4_admin_ci_variables_key) | **PUT** /api/v4/admin/ci/variables/{key} | 


# **delete_api_v4_admin_ci_variables_key**
> APIEntitiesCiVariable delete_api_v4_admin_ci_variables_key(key)



Delete an existing instance-level variable

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_ci_variable import APIEntitiesCiVariable
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
    api_instance = openapi_client.CiVariablesApi(api_client)
    key = 'key_example' # str | The key of a variable

    try:
        api_response = api_instance.delete_api_v4_admin_ci_variables_key(key)
        print("The response of CiVariablesApi->delete_api_v4_admin_ci_variables_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CiVariablesApi->delete_api_v4_admin_ci_variables_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of a variable | 

### Return type

[**APIEntitiesCiVariable**](APIEntitiesCiVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Delete an existing instance-level variable |  -  |
**404** | Instance Variable Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_admin_ci_variables**
> APIEntitiesCiVariable get_api_v4_admin_ci_variables(page=page, per_page=per_page)



List all instance-level variables

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_ci_variable import APIEntitiesCiVariable
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
    api_instance = openapi_client.CiVariablesApi(api_client)
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)

    try:
        api_response = api_instance.get_api_v4_admin_ci_variables(page=page, per_page=per_page)
        print("The response of CiVariablesApi->get_api_v4_admin_ci_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CiVariablesApi->get_api_v4_admin_ci_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]

### Return type

[**APIEntitiesCiVariable**](APIEntitiesCiVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all instance-level variables |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_admin_ci_variables_key**
> APIEntitiesCiVariable get_api_v4_admin_ci_variables_key(key)



Get the details of a specific instance-level variable

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_ci_variable import APIEntitiesCiVariable
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
    api_instance = openapi_client.CiVariablesApi(api_client)
    key = 'key_example' # str | The key of a variable

    try:
        api_response = api_instance.get_api_v4_admin_ci_variables_key(key)
        print("The response of CiVariablesApi->get_api_v4_admin_ci_variables_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CiVariablesApi->get_api_v4_admin_ci_variables_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of a variable | 

### Return type

[**APIEntitiesCiVariable**](APIEntitiesCiVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the details of a specific instance-level variable |  -  |
**404** | Instance Variable Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_admin_ci_variables**
> APIEntitiesCiVariable post_api_v4_admin_ci_variables(post_api_v4_admin_ci_variables_request)



Create a new instance-level variable

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_ci_variable import APIEntitiesCiVariable
from openapi_client.models.post_api_v4_admin_ci_variables_request import PostApiV4AdminCiVariablesRequest
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
    api_instance = openapi_client.CiVariablesApi(api_client)
    post_api_v4_admin_ci_variables_request = openapi_client.PostApiV4AdminCiVariablesRequest() # PostApiV4AdminCiVariablesRequest | 

    try:
        api_response = api_instance.post_api_v4_admin_ci_variables(post_api_v4_admin_ci_variables_request)
        print("The response of CiVariablesApi->post_api_v4_admin_ci_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CiVariablesApi->post_api_v4_admin_ci_variables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_api_v4_admin_ci_variables_request** | [**PostApiV4AdminCiVariablesRequest**](PostApiV4AdminCiVariablesRequest.md)|  | 

### Return type

[**APIEntitiesCiVariable**](APIEntitiesCiVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new instance-level variable |  -  |
**400** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_admin_ci_variables_key**
> APIEntitiesCiVariable put_api_v4_admin_ci_variables_key(key, put_api_v4_admin_ci_variables_key_request=put_api_v4_admin_ci_variables_key_request)



Update an instance-level variable

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_ci_variable import APIEntitiesCiVariable
from openapi_client.models.put_api_v4_admin_ci_variables_key_request import PutApiV4AdminCiVariablesKeyRequest
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
    api_instance = openapi_client.CiVariablesApi(api_client)
    key = 'key_example' # str | The key of a variable
    put_api_v4_admin_ci_variables_key_request = openapi_client.PutApiV4AdminCiVariablesKeyRequest() # PutApiV4AdminCiVariablesKeyRequest |  (optional)

    try:
        api_response = api_instance.put_api_v4_admin_ci_variables_key(key, put_api_v4_admin_ci_variables_key_request=put_api_v4_admin_ci_variables_key_request)
        print("The response of CiVariablesApi->put_api_v4_admin_ci_variables_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CiVariablesApi->put_api_v4_admin_ci_variables_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of a variable | 
 **put_api_v4_admin_ci_variables_key_request** | [**PutApiV4AdminCiVariablesKeyRequest**](PutApiV4AdminCiVariablesKeyRequest.md)|  | [optional] 

### Return type

[**APIEntitiesCiVariable**](APIEntitiesCiVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update an instance-level variable |  -  |
**404** | Instance Variable Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

