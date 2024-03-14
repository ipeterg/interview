# openapi_client.ApplicationsApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_applications_id**](ApplicationsApi.md#delete_api_v4_applications_id) | **DELETE** /api/v4/applications/{id} | Delete an application
[**get_api_v4_applications**](ApplicationsApi.md#get_api_v4_applications) | **GET** /api/v4/applications | Get applications
[**post_api_v4_applications**](ApplicationsApi.md#post_api_v4_applications) | **POST** /api/v4/applications | Create a new application


# **delete_api_v4_applications_id**
> delete_api_v4_applications_id(id)

Delete an application

Delete a specific application

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    id = 56 # int | The ID of the application (not the application_id)

    try:
        # Delete an application
        api_instance.delete_api_v4_applications_id(id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_api_v4_applications_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the application (not the application_id) | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Delete an application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_applications**
> List[APIEntitiesApplication] get_api_v4_applications()

Get applications

List all registered applications

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_application import APIEntitiesApplication
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
    api_instance = openapi_client.ApplicationsApi(api_client)

    try:
        # Get applications
        api_response = api_instance.get_api_v4_applications()
        print("The response of ApplicationsApi->get_api_v4_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_api_v4_applications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[APIEntitiesApplication]**](APIEntitiesApplication.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get applications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_applications**
> APIEntitiesApplicationWithSecret post_api_v4_applications(post_api_v4_applications_request)

Create a new application

This feature was introduced in GitLab 10.5

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_application_with_secret import APIEntitiesApplicationWithSecret
from openapi_client.models.post_api_v4_applications_request import PostApiV4ApplicationsRequest
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
    api_instance = openapi_client.ApplicationsApi(api_client)
    post_api_v4_applications_request = openapi_client.PostApiV4ApplicationsRequest() # PostApiV4ApplicationsRequest | 

    try:
        # Create a new application
        api_response = api_instance.post_api_v4_applications(post_api_v4_applications_request)
        print("The response of ApplicationsApi->post_api_v4_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->post_api_v4_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_api_v4_applications_request** | [**PostApiV4ApplicationsRequest**](PostApiV4ApplicationsRequest.md)|  | 

### Return type

[**APIEntitiesApplicationWithSecret**](APIEntitiesApplicationWithSecret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a new application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

