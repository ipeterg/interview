# openapi_client.BroadcastMessagesApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_broadcast_messages_id**](BroadcastMessagesApi.md#delete_api_v4_broadcast_messages_id) | **DELETE** /api/v4/broadcast_messages/{id} | Delete a broadcast message
[**get_api_v4_broadcast_messages**](BroadcastMessagesApi.md#get_api_v4_broadcast_messages) | **GET** /api/v4/broadcast_messages | Get all broadcast messages
[**get_api_v4_broadcast_messages_id**](BroadcastMessagesApi.md#get_api_v4_broadcast_messages_id) | **GET** /api/v4/broadcast_messages/{id} | Get a specific broadcast message
[**post_api_v4_broadcast_messages**](BroadcastMessagesApi.md#post_api_v4_broadcast_messages) | **POST** /api/v4/broadcast_messages | Create a broadcast message
[**put_api_v4_broadcast_messages_id**](BroadcastMessagesApi.md#put_api_v4_broadcast_messages_id) | **PUT** /api/v4/broadcast_messages/{id} | Update a broadcast message


# **delete_api_v4_broadcast_messages_id**
> APIEntitiesBroadcastMessage delete_api_v4_broadcast_messages_id(id)

Delete a broadcast message

This feature was introduced in GitLab 8.12.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_broadcast_message import APIEntitiesBroadcastMessage
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
    api_instance = openapi_client.BroadcastMessagesApi(api_client)
    id = 56 # int | Broadcast message ID

    try:
        # Delete a broadcast message
        api_response = api_instance.delete_api_v4_broadcast_messages_id(id)
        print("The response of BroadcastMessagesApi->delete_api_v4_broadcast_messages_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastMessagesApi->delete_api_v4_broadcast_messages_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Broadcast message ID | 

### Return type

[**APIEntitiesBroadcastMessage**](APIEntitiesBroadcastMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a broadcast message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_broadcast_messages**
> APIEntitiesBroadcastMessage get_api_v4_broadcast_messages(page=page, per_page=per_page)

Get all broadcast messages

This feature was introduced in GitLab 8.12.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_broadcast_message import APIEntitiesBroadcastMessage
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
    api_instance = openapi_client.BroadcastMessagesApi(api_client)
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)

    try:
        # Get all broadcast messages
        api_response = api_instance.get_api_v4_broadcast_messages(page=page, per_page=per_page)
        print("The response of BroadcastMessagesApi->get_api_v4_broadcast_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastMessagesApi->get_api_v4_broadcast_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]

### Return type

[**APIEntitiesBroadcastMessage**](APIEntitiesBroadcastMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get all broadcast messages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_broadcast_messages_id**
> APIEntitiesBroadcastMessage get_api_v4_broadcast_messages_id(id)

Get a specific broadcast message

This feature was introduced in GitLab 8.12.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_broadcast_message import APIEntitiesBroadcastMessage
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
    api_instance = openapi_client.BroadcastMessagesApi(api_client)
    id = 56 # int | Broadcast message ID

    try:
        # Get a specific broadcast message
        api_response = api_instance.get_api_v4_broadcast_messages_id(id)
        print("The response of BroadcastMessagesApi->get_api_v4_broadcast_messages_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastMessagesApi->get_api_v4_broadcast_messages_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Broadcast message ID | 

### Return type

[**APIEntitiesBroadcastMessage**](APIEntitiesBroadcastMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a specific broadcast message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_broadcast_messages**
> APIEntitiesBroadcastMessage post_api_v4_broadcast_messages(post_api_v4_broadcast_messages_request)

Create a broadcast message

This feature was introduced in GitLab 8.12.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_broadcast_message import APIEntitiesBroadcastMessage
from openapi_client.models.post_api_v4_broadcast_messages_request import PostApiV4BroadcastMessagesRequest
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
    api_instance = openapi_client.BroadcastMessagesApi(api_client)
    post_api_v4_broadcast_messages_request = openapi_client.PostApiV4BroadcastMessagesRequest() # PostApiV4BroadcastMessagesRequest | 

    try:
        # Create a broadcast message
        api_response = api_instance.post_api_v4_broadcast_messages(post_api_v4_broadcast_messages_request)
        print("The response of BroadcastMessagesApi->post_api_v4_broadcast_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastMessagesApi->post_api_v4_broadcast_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_api_v4_broadcast_messages_request** | [**PostApiV4BroadcastMessagesRequest**](PostApiV4BroadcastMessagesRequest.md)|  | 

### Return type

[**APIEntitiesBroadcastMessage**](APIEntitiesBroadcastMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a broadcast message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_broadcast_messages_id**
> APIEntitiesBroadcastMessage put_api_v4_broadcast_messages_id(id, put_api_v4_broadcast_messages_id_request=put_api_v4_broadcast_messages_id_request)

Update a broadcast message

This feature was introduced in GitLab 8.12.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_broadcast_message import APIEntitiesBroadcastMessage
from openapi_client.models.put_api_v4_broadcast_messages_id_request import PutApiV4BroadcastMessagesIdRequest
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
    api_instance = openapi_client.BroadcastMessagesApi(api_client)
    id = 56 # int | Broadcast message ID
    put_api_v4_broadcast_messages_id_request = openapi_client.PutApiV4BroadcastMessagesIdRequest() # PutApiV4BroadcastMessagesIdRequest |  (optional)

    try:
        # Update a broadcast message
        api_response = api_instance.put_api_v4_broadcast_messages_id(id, put_api_v4_broadcast_messages_id_request=put_api_v4_broadcast_messages_id_request)
        print("The response of BroadcastMessagesApi->put_api_v4_broadcast_messages_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastMessagesApi->put_api_v4_broadcast_messages_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Broadcast message ID | 
 **put_api_v4_broadcast_messages_id_request** | [**PutApiV4BroadcastMessagesIdRequest**](PutApiV4BroadcastMessagesIdRequest.md)|  | [optional] 

### Return type

[**APIEntitiesBroadcastMessage**](APIEntitiesBroadcastMessage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a broadcast message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

