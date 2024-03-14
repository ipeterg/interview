# openapi_client.BadgesApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_groups_id_badges_badge_id**](BadgesApi.md#delete_api_v4_groups_id_badges_badge_id) | **DELETE** /api/v4/groups/{id}/badges/{badge_id} | Removes a badge from the group.
[**delete_api_v4_projects_id_badges_badge_id**](BadgesApi.md#delete_api_v4_projects_id_badges_badge_id) | **DELETE** /api/v4/projects/{id}/badges/{badge_id} | Removes a badge from the project.
[**get_api_v4_groups_id_badges**](BadgesApi.md#get_api_v4_groups_id_badges) | **GET** /api/v4/groups/{id}/badges | Gets a list of group badges viewable by the authenticated user.
[**get_api_v4_groups_id_badges_badge_id**](BadgesApi.md#get_api_v4_groups_id_badges_badge_id) | **GET** /api/v4/groups/{id}/badges/{badge_id} | Gets a badge of a group.
[**get_api_v4_groups_id_badges_render**](BadgesApi.md#get_api_v4_groups_id_badges_render) | **GET** /api/v4/groups/{id}/badges/render | Preview a badge from a group.
[**get_api_v4_projects_id_badges**](BadgesApi.md#get_api_v4_projects_id_badges) | **GET** /api/v4/projects/{id}/badges | Gets a list of project badges viewable by the authenticated user.
[**get_api_v4_projects_id_badges_badge_id**](BadgesApi.md#get_api_v4_projects_id_badges_badge_id) | **GET** /api/v4/projects/{id}/badges/{badge_id} | Gets a badge of a project.
[**get_api_v4_projects_id_badges_render**](BadgesApi.md#get_api_v4_projects_id_badges_render) | **GET** /api/v4/projects/{id}/badges/render | Preview a badge from a project.
[**post_api_v4_groups_id_badges**](BadgesApi.md#post_api_v4_groups_id_badges) | **POST** /api/v4/groups/{id}/badges | Adds a badge to a group.
[**post_api_v4_projects_id_badges**](BadgesApi.md#post_api_v4_projects_id_badges) | **POST** /api/v4/projects/{id}/badges | Adds a badge to a project.
[**put_api_v4_groups_id_badges_badge_id**](BadgesApi.md#put_api_v4_groups_id_badges_badge_id) | **PUT** /api/v4/groups/{id}/badges/{badge_id} | Updates a badge of a group.
[**put_api_v4_projects_id_badges_badge_id**](BadgesApi.md#put_api_v4_projects_id_badges_badge_id) | **PUT** /api/v4/projects/{id}/badges/{badge_id} | Updates a badge of a project.


# **delete_api_v4_groups_id_badges_badge_id**
> delete_api_v4_groups_id_badges_badge_id(id, badge_id)

Removes a badge from the group.

This feature was introduced in GitLab 10.6.

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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user.
    badge_id = 56 # int | The badge ID

    try:
        # Removes a badge from the group.
        api_instance.delete_api_v4_groups_id_badges_badge_id(id, badge_id)
    except Exception as e:
        print("Exception when calling BadgesApi->delete_api_v4_groups_id_badges_badge_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user. | 
 **badge_id** | **int**| The badge ID | 

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
**204** | Removes a badge from the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_v4_projects_id_badges_badge_id**
> delete_api_v4_projects_id_badges_badge_id(id, badge_id)

Removes a badge from the project.

This feature was introduced in GitLab 10.6.

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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user.
    badge_id = 56 # int | The badge ID

    try:
        # Removes a badge from the project.
        api_instance.delete_api_v4_projects_id_badges_badge_id(id, badge_id)
    except Exception as e:
        print("Exception when calling BadgesApi->delete_api_v4_projects_id_badges_badge_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user. | 
 **badge_id** | **int**| The badge ID | 

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
**204** | Removes a badge from the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_groups_id_badges**
> List[APIEntitiesBadge] get_api_v4_groups_id_badges(id, page=page, per_page=per_page, name=name)

Gets a list of group badges viewable by the authenticated user.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user.
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)
    name = 'name_example' # str | Name for the badge (optional)

    try:
        # Gets a list of group badges viewable by the authenticated user.
        api_response = api_instance.get_api_v4_groups_id_badges(id, page=page, per_page=per_page, name=name)
        print("The response of BadgesApi->get_api_v4_groups_id_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->get_api_v4_groups_id_badges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user. | 
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]
 **name** | **str**| Name for the badge | [optional] 

### Return type

[**List[APIEntitiesBadge]**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of group badges viewable by the authenticated user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_groups_id_badges_badge_id**
> APIEntitiesBadge get_api_v4_groups_id_badges_badge_id(id, badge_id)

Gets a badge of a group.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user.
    badge_id = 56 # int | The badge ID

    try:
        # Gets a badge of a group.
        api_response = api_instance.get_api_v4_groups_id_badges_badge_id(id, badge_id)
        print("The response of BadgesApi->get_api_v4_groups_id_badges_badge_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->get_api_v4_groups_id_badges_badge_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user. | 
 **badge_id** | **int**| The badge ID | 

### Return type

[**APIEntitiesBadge**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a badge of a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_groups_id_badges_render**
> APIEntitiesBasicBadgeDetails get_api_v4_groups_id_badges_render(id, link_url, image_url)

Preview a badge from a group.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_basic_badge_details import APIEntitiesBasicBadgeDetails
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user.
    link_url = 'link_url_example' # str | URL of the badge link
    image_url = 'image_url_example' # str | URL of the badge image

    try:
        # Preview a badge from a group.
        api_response = api_instance.get_api_v4_groups_id_badges_render(id, link_url, image_url)
        print("The response of BadgesApi->get_api_v4_groups_id_badges_render:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->get_api_v4_groups_id_badges_render: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user. | 
 **link_url** | **str**| URL of the badge link | 
 **image_url** | **str**| URL of the badge image | 

### Return type

[**APIEntitiesBasicBadgeDetails**](APIEntitiesBasicBadgeDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview a badge from a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_projects_id_badges**
> List[APIEntitiesBadge] get_api_v4_projects_id_badges(id, page=page, per_page=per_page, name=name)

Gets a list of project badges viewable by the authenticated user.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user.
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)
    name = 'name_example' # str | Name for the badge (optional)

    try:
        # Gets a list of project badges viewable by the authenticated user.
        api_response = api_instance.get_api_v4_projects_id_badges(id, page=page, per_page=per_page, name=name)
        print("The response of BadgesApi->get_api_v4_projects_id_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->get_api_v4_projects_id_badges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user. | 
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]
 **name** | **str**| Name for the badge | [optional] 

### Return type

[**List[APIEntitiesBadge]**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of project badges viewable by the authenticated user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_projects_id_badges_badge_id**
> APIEntitiesBadge get_api_v4_projects_id_badges_badge_id(id, badge_id)

Gets a badge of a project.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user.
    badge_id = 56 # int | The badge ID

    try:
        # Gets a badge of a project.
        api_response = api_instance.get_api_v4_projects_id_badges_badge_id(id, badge_id)
        print("The response of BadgesApi->get_api_v4_projects_id_badges_badge_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->get_api_v4_projects_id_badges_badge_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user. | 
 **badge_id** | **int**| The badge ID | 

### Return type

[**APIEntitiesBadge**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a badge of a project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_projects_id_badges_render**
> APIEntitiesBasicBadgeDetails get_api_v4_projects_id_badges_render(id, link_url, image_url)

Preview a badge from a project.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_basic_badge_details import APIEntitiesBasicBadgeDetails
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user.
    link_url = 'link_url_example' # str | URL of the badge link
    image_url = 'image_url_example' # str | URL of the badge image

    try:
        # Preview a badge from a project.
        api_response = api_instance.get_api_v4_projects_id_badges_render(id, link_url, image_url)
        print("The response of BadgesApi->get_api_v4_projects_id_badges_render:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->get_api_v4_projects_id_badges_render: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user. | 
 **link_url** | **str**| URL of the badge link | 
 **image_url** | **str**| URL of the badge image | 

### Return type

[**APIEntitiesBasicBadgeDetails**](APIEntitiesBasicBadgeDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview a badge from a project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_groups_id_badges**
> APIEntitiesBadge post_api_v4_groups_id_badges(id, post_api_v4_groups_id_badges_request)

Adds a badge to a group.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
from openapi_client.models.post_api_v4_groups_id_badges_request import PostApiV4GroupsIdBadgesRequest
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user.
    post_api_v4_groups_id_badges_request = openapi_client.PostApiV4GroupsIdBadgesRequest() # PostApiV4GroupsIdBadgesRequest | 

    try:
        # Adds a badge to a group.
        api_response = api_instance.post_api_v4_groups_id_badges(id, post_api_v4_groups_id_badges_request)
        print("The response of BadgesApi->post_api_v4_groups_id_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->post_api_v4_groups_id_badges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user. | 
 **post_api_v4_groups_id_badges_request** | [**PostApiV4GroupsIdBadgesRequest**](PostApiV4GroupsIdBadgesRequest.md)|  | 

### Return type

[**APIEntitiesBadge**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Adds a badge to a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_projects_id_badges**
> APIEntitiesBadge post_api_v4_projects_id_badges(id, post_api_v4_groups_id_badges_request)

Adds a badge to a project.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
from openapi_client.models.post_api_v4_groups_id_badges_request import PostApiV4GroupsIdBadgesRequest
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user.
    post_api_v4_groups_id_badges_request = openapi_client.PostApiV4GroupsIdBadgesRequest() # PostApiV4GroupsIdBadgesRequest | 

    try:
        # Adds a badge to a project.
        api_response = api_instance.post_api_v4_projects_id_badges(id, post_api_v4_groups_id_badges_request)
        print("The response of BadgesApi->post_api_v4_projects_id_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->post_api_v4_projects_id_badges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user. | 
 **post_api_v4_groups_id_badges_request** | [**PostApiV4GroupsIdBadgesRequest**](PostApiV4GroupsIdBadgesRequest.md)|  | 

### Return type

[**APIEntitiesBadge**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Adds a badge to a project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_groups_id_badges_badge_id**
> APIEntitiesBadge put_api_v4_groups_id_badges_badge_id(id, badge_id, put_api_v4_groups_id_badges_badge_id_request=put_api_v4_groups_id_badges_badge_id_request)

Updates a badge of a group.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
from openapi_client.models.put_api_v4_groups_id_badges_badge_id_request import PutApiV4GroupsIdBadgesBadgeIdRequest
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the group owned by the authenticated user.
    badge_id = 56 # int | 
    put_api_v4_groups_id_badges_badge_id_request = openapi_client.PutApiV4GroupsIdBadgesBadgeIdRequest() # PutApiV4GroupsIdBadgesBadgeIdRequest |  (optional)

    try:
        # Updates a badge of a group.
        api_response = api_instance.put_api_v4_groups_id_badges_badge_id(id, badge_id, put_api_v4_groups_id_badges_badge_id_request=put_api_v4_groups_id_badges_badge_id_request)
        print("The response of BadgesApi->put_api_v4_groups_id_badges_badge_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->put_api_v4_groups_id_badges_badge_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the group owned by the authenticated user. | 
 **badge_id** | **int**|  | 
 **put_api_v4_groups_id_badges_badge_id_request** | [**PutApiV4GroupsIdBadgesBadgeIdRequest**](PutApiV4GroupsIdBadgesBadgeIdRequest.md)|  | [optional] 

### Return type

[**APIEntitiesBadge**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a badge of a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_projects_id_badges_badge_id**
> APIEntitiesBadge put_api_v4_projects_id_badges_badge_id(id, badge_id, put_api_v4_groups_id_badges_badge_id_request=put_api_v4_groups_id_badges_badge_id_request)

Updates a badge of a project.

This feature was introduced in GitLab 10.6.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_badge import APIEntitiesBadge
from openapi_client.models.put_api_v4_groups_id_badges_badge_id_request import PutApiV4GroupsIdBadgesBadgeIdRequest
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
    api_instance = openapi_client.BadgesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project owned by the authenticated user.
    badge_id = 56 # int | 
    put_api_v4_groups_id_badges_badge_id_request = openapi_client.PutApiV4GroupsIdBadgesBadgeIdRequest() # PutApiV4GroupsIdBadgesBadgeIdRequest |  (optional)

    try:
        # Updates a badge of a project.
        api_response = api_instance.put_api_v4_projects_id_badges_badge_id(id, badge_id, put_api_v4_groups_id_badges_badge_id_request=put_api_v4_groups_id_badges_badge_id_request)
        print("The response of BadgesApi->put_api_v4_projects_id_badges_badge_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadgesApi->put_api_v4_projects_id_badges_badge_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project owned by the authenticated user. | 
 **badge_id** | **int**|  | 
 **put_api_v4_groups_id_badges_badge_id_request** | [**PutApiV4GroupsIdBadgesBadgeIdRequest**](PutApiV4GroupsIdBadgesBadgeIdRequest.md)|  | [optional] 

### Return type

[**APIEntitiesBadge**](APIEntitiesBadge.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a badge of a project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

