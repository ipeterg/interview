# openapi_client.AccessRequestsApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_groups_id_access_requests_user_id**](AccessRequestsApi.md#delete_api_v4_groups_id_access_requests_user_id) | **DELETE** /api/v4/groups/{id}/access_requests/{user_id} | Denies an access request for the given user.
[**delete_api_v4_projects_id_access_requests_user_id**](AccessRequestsApi.md#delete_api_v4_projects_id_access_requests_user_id) | **DELETE** /api/v4/projects/{id}/access_requests/{user_id} | Denies an access request for the given user.
[**get_api_v4_groups_id_access_requests**](AccessRequestsApi.md#get_api_v4_groups_id_access_requests) | **GET** /api/v4/groups/{id}/access_requests | Gets a list of access requests for a group.
[**get_api_v4_projects_id_access_requests**](AccessRequestsApi.md#get_api_v4_projects_id_access_requests) | **GET** /api/v4/projects/{id}/access_requests | Gets a list of access requests for a project.
[**post_api_v4_groups_id_access_requests**](AccessRequestsApi.md#post_api_v4_groups_id_access_requests) | **POST** /api/v4/groups/{id}/access_requests | Requests access for the authenticated user to a group.
[**post_api_v4_projects_id_access_requests**](AccessRequestsApi.md#post_api_v4_projects_id_access_requests) | **POST** /api/v4/projects/{id}/access_requests | Requests access for the authenticated user to a project.
[**put_api_v4_groups_id_access_requests_user_id_approve**](AccessRequestsApi.md#put_api_v4_groups_id_access_requests_user_id_approve) | **PUT** /api/v4/groups/{id}/access_requests/{user_id}/approve | Approves an access request for the given user.
[**put_api_v4_projects_id_access_requests_user_id_approve**](AccessRequestsApi.md#put_api_v4_projects_id_access_requests_user_id_approve) | **PUT** /api/v4/projects/{id}/access_requests/{user_id}/approve | Approves an access request for the given user.


# **delete_api_v4_groups_id_access_requests_user_id**
> delete_api_v4_groups_id_access_requests_user_id(id, user_id)

Denies an access request for the given user.

This feature was introduced in GitLab 8.11.

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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user
    user_id = 56 # int | The user ID of the access requester

    try:
        # Denies an access request for the given user.
        api_instance.delete_api_v4_groups_id_access_requests_user_id(id, user_id)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->delete_api_v4_groups_id_access_requests_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user | 
 **user_id** | **int**| The user ID of the access requester | 

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
**204** | Denies an access request for the given user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_v4_projects_id_access_requests_user_id**
> delete_api_v4_projects_id_access_requests_user_id(id, user_id)

Denies an access request for the given user.

This feature was introduced in GitLab 8.11.

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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user
    user_id = 56 # int | The user ID of the access requester

    try:
        # Denies an access request for the given user.
        api_instance.delete_api_v4_projects_id_access_requests_user_id(id, user_id)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->delete_api_v4_projects_id_access_requests_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user | 
 **user_id** | **int**| The user ID of the access requester | 

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
**204** | Denies an access request for the given user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_groups_id_access_requests**
> APIEntitiesAccessRequester get_api_v4_groups_id_access_requests(id, page=page, per_page=per_page)

Gets a list of access requests for a group.

This feature was introduced in GitLab 8.11.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_access_requester import APIEntitiesAccessRequester
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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)

    try:
        # Gets a list of access requests for a group.
        api_response = api_instance.get_api_v4_groups_id_access_requests(id, page=page, per_page=per_page)
        print("The response of AccessRequestsApi->get_api_v4_groups_id_access_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->get_api_v4_groups_id_access_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user | 
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]

### Return type

[**APIEntitiesAccessRequester**](APIEntitiesAccessRequester.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of access requests for a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_projects_id_access_requests**
> APIEntitiesAccessRequester get_api_v4_projects_id_access_requests(id, page=page, per_page=per_page)

Gets a list of access requests for a project.

This feature was introduced in GitLab 8.11.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_access_requester import APIEntitiesAccessRequester
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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)

    try:
        # Gets a list of access requests for a project.
        api_response = api_instance.get_api_v4_projects_id_access_requests(id, page=page, per_page=per_page)
        print("The response of AccessRequestsApi->get_api_v4_projects_id_access_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->get_api_v4_projects_id_access_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user | 
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]

### Return type

[**APIEntitiesAccessRequester**](APIEntitiesAccessRequester.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of access requests for a project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_groups_id_access_requests**
> APIEntitiesAccessRequester post_api_v4_groups_id_access_requests(id)

Requests access for the authenticated user to a group.

This feature was introduced in GitLab 8.11.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_access_requester import APIEntitiesAccessRequester
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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user

    try:
        # Requests access for the authenticated user to a group.
        api_response = api_instance.post_api_v4_groups_id_access_requests(id)
        print("The response of AccessRequestsApi->post_api_v4_groups_id_access_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->post_api_v4_groups_id_access_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user | 

### Return type

[**APIEntitiesAccessRequester**](APIEntitiesAccessRequester.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, successfull_response

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_projects_id_access_requests**
> APIEntitiesAccessRequester post_api_v4_projects_id_access_requests(id)

Requests access for the authenticated user to a project.

This feature was introduced in GitLab 8.11.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_access_requester import APIEntitiesAccessRequester
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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user

    try:
        # Requests access for the authenticated user to a project.
        api_response = api_instance.post_api_v4_projects_id_access_requests(id)
        print("The response of AccessRequestsApi->post_api_v4_projects_id_access_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->post_api_v4_projects_id_access_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user | 

### Return type

[**APIEntitiesAccessRequester**](APIEntitiesAccessRequester.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, successfull_response

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_groups_id_access_requests_user_id_approve**
> APIEntitiesAccessRequester put_api_v4_groups_id_access_requests_user_id_approve(id, user_id, put_api_v4_groups_id_access_requests_user_id_approve_request=put_api_v4_groups_id_access_requests_user_id_approve_request)

Approves an access request for the given user.

This feature was introduced in GitLab 8.11.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_access_requester import APIEntitiesAccessRequester
from openapi_client.models.put_api_v4_groups_id_access_requests_user_id_approve_request import PutApiV4GroupsIdAccessRequestsUserIdApproveRequest
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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user
    user_id = 56 # int | The user ID of the access requester
    put_api_v4_groups_id_access_requests_user_id_approve_request = openapi_client.PutApiV4GroupsIdAccessRequestsUserIdApproveRequest() # PutApiV4GroupsIdAccessRequestsUserIdApproveRequest |  (optional)

    try:
        # Approves an access request for the given user.
        api_response = api_instance.put_api_v4_groups_id_access_requests_user_id_approve(id, user_id, put_api_v4_groups_id_access_requests_user_id_approve_request=put_api_v4_groups_id_access_requests_user_id_approve_request)
        print("The response of AccessRequestsApi->put_api_v4_groups_id_access_requests_user_id_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->put_api_v4_groups_id_access_requests_user_id_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user | 
 **user_id** | **int**| The user ID of the access requester | 
 **put_api_v4_groups_id_access_requests_user_id_approve_request** | [**PutApiV4GroupsIdAccessRequestsUserIdApproveRequest**](PutApiV4GroupsIdAccessRequestsUserIdApproveRequest.md)|  | [optional] 

### Return type

[**APIEntitiesAccessRequester**](APIEntitiesAccessRequester.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, successfull_response

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_projects_id_access_requests_user_id_approve**
> APIEntitiesAccessRequester put_api_v4_projects_id_access_requests_user_id_approve(id, user_id, put_api_v4_groups_id_access_requests_user_id_approve_request=put_api_v4_groups_id_access_requests_user_id_approve_request)

Approves an access request for the given user.

This feature was introduced in GitLab 8.11.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_access_requester import APIEntitiesAccessRequester
from openapi_client.models.put_api_v4_groups_id_access_requests_user_id_approve_request import PutApiV4GroupsIdAccessRequestsUserIdApproveRequest
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
    api_instance = openapi_client.AccessRequestsApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user
    user_id = 56 # int | The user ID of the access requester
    put_api_v4_groups_id_access_requests_user_id_approve_request = openapi_client.PutApiV4GroupsIdAccessRequestsUserIdApproveRequest() # PutApiV4GroupsIdAccessRequestsUserIdApproveRequest |  (optional)

    try:
        # Approves an access request for the given user.
        api_response = api_instance.put_api_v4_projects_id_access_requests_user_id_approve(id, user_id, put_api_v4_groups_id_access_requests_user_id_approve_request=put_api_v4_groups_id_access_requests_user_id_approve_request)
        print("The response of AccessRequestsApi->put_api_v4_projects_id_access_requests_user_id_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessRequestsApi->put_api_v4_projects_id_access_requests_user_id_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user | 
 **user_id** | **int**| The user ID of the access requester | 
 **put_api_v4_groups_id_access_requests_user_id_approve_request** | [**PutApiV4GroupsIdAccessRequestsUserIdApproveRequest**](PutApiV4GroupsIdAccessRequestsUserIdApproveRequest.md)|  | [optional] 

### Return type

[**APIEntitiesAccessRequester**](APIEntitiesAccessRequester.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, successfull_response

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

