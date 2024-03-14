# openapi_client.AvatarApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v4_avatar**](AvatarApi.md#get_api_v4_avatar) | **GET** /api/v4/avatar | 


# **get_api_v4_avatar**
> APIEntitiesAvatar get_api_v4_avatar(email, size=size)



Return avatar url for a user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_avatar import APIEntitiesAvatar
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
    api_instance = openapi_client.AvatarApi(api_client)
    email = 'email_example' # str | Public email address of the user
    size = 56 # int | Single pixel dimension for Gravatar images (optional)

    try:
        api_response = api_instance.get_api_v4_avatar(email, size=size)
        print("The response of AvatarApi->get_api_v4_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarApi->get_api_v4_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Public email address of the user | 
 **size** | **int**| Single pixel dimension for Gravatar images | [optional] 

### Return type

[**APIEntitiesAvatar**](APIEntitiesAvatar.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return avatar url for a user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

