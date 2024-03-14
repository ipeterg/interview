# openapi_client.MetadataApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v4_metadata**](MetadataApi.md#get_api_v4_metadata) | **GET** /api/v4/metadata | Retrieve metadata information for this GitLab instance
[**get_api_v4_version**](MetadataApi.md#get_api_v4_version) | **GET** /api/v4/version | Retrieves version information for the GitLab instance


# **get_api_v4_metadata**
> APIEntitiesMetadata get_api_v4_metadata()

Retrieve metadata information for this GitLab instance

This feature was introduced in GitLab 15.2.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_metadata import APIEntitiesMetadata
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
    api_instance = openapi_client.MetadataApi(api_client)

    try:
        # Retrieve metadata information for this GitLab instance
        api_response = api_instance.get_api_v4_metadata()
        print("The response of MetadataApi->get_api_v4_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_api_v4_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIEntitiesMetadata**](APIEntitiesMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve metadata information for this GitLab instance |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_version**
> APIEntitiesMetadata get_api_v4_version()

Retrieves version information for the GitLab instance

This feature was introduced in GitLab 8.13 and deprecated in 15.5. We recommend you instead use the Metadata API.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_metadata import APIEntitiesMetadata
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
    api_instance = openapi_client.MetadataApi(api_client)

    try:
        # Retrieves version information for the GitLab instance
        api_response = api_instance.get_api_v4_version()
        print("The response of MetadataApi->get_api_v4_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_api_v4_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIEntitiesMetadata**](APIEntitiesMetadata.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves version information for the GitLab instance |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

