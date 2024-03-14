# openapi_client.BranchesApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_projects_id_repository_branches_branch**](BranchesApi.md#delete_api_v4_projects_id_repository_branches_branch) | **DELETE** /api/v4/projects/{id}/repository/branches/{branch} | 
[**delete_api_v4_projects_id_repository_merged_branches**](BranchesApi.md#delete_api_v4_projects_id_repository_merged_branches) | **DELETE** /api/v4/projects/{id}/repository/merged_branches | 
[**get_api_v4_projects_id_repository_branches**](BranchesApi.md#get_api_v4_projects_id_repository_branches) | **GET** /api/v4/projects/{id}/repository/branches | 
[**get_api_v4_projects_id_repository_branches_branch**](BranchesApi.md#get_api_v4_projects_id_repository_branches_branch) | **GET** /api/v4/projects/{id}/repository/branches/{branch} | 
[**head_api_v4_projects_id_repository_branches_branch**](BranchesApi.md#head_api_v4_projects_id_repository_branches_branch) | **HEAD** /api/v4/projects/{id}/repository/branches/{branch} | 
[**post_api_v4_projects_id_repository_branches**](BranchesApi.md#post_api_v4_projects_id_repository_branches) | **POST** /api/v4/projects/{id}/repository/branches | 
[**put_api_v4_projects_id_repository_branches_branch_protect**](BranchesApi.md#put_api_v4_projects_id_repository_branches_branch_protect) | **PUT** /api/v4/projects/{id}/repository/branches/{branch}/protect | 
[**put_api_v4_projects_id_repository_branches_branch_unprotect**](BranchesApi.md#put_api_v4_projects_id_repository_branches_branch_unprotect) | **PUT** /api/v4/projects/{id}/repository/branches/{branch}/unprotect | 


# **delete_api_v4_projects_id_repository_branches_branch**
> delete_api_v4_projects_id_repository_branches_branch(id, branch)



Delete a branch

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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    branch = 'branch_example' # str | The name of the branch

    try:
        api_instance.delete_api_v4_projects_id_repository_branches_branch(id, branch)
    except Exception as e:
        print("Exception when calling BranchesApi->delete_api_v4_projects_id_repository_branches_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **branch** | **str**| The name of the branch | 

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
**204** | Delete a branch |  -  |
**404** | Branch Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_v4_projects_id_repository_merged_branches**
> delete_api_v4_projects_id_repository_merged_branches(id)



Delete all merged branches

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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project

    try:
        api_instance.delete_api_v4_projects_id_repository_merged_branches(id)
    except Exception as e:
        print("Exception when calling BranchesApi->delete_api_v4_projects_id_repository_merged_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 

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
**202** | 202 Accepted |  -  |
**404** | 404 Project Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_projects_id_repository_branches**
> List[APIEntitiesBranch] get_api_v4_projects_id_repository_branches(id, page=page, per_page=per_page, search=search, regex=regex, sort=sort, page_token=page_token)



Get a project repository branches

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_branch import APIEntitiesBranch
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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    page = 1 # int | Current page number (optional) (default to 1)
    per_page = 20 # int | Number of items per page (optional) (default to 20)
    search = 'search_example' # str | Return list of branches matching the search criteria (optional)
    regex = 'regex_example' # str | Return list of branches matching the regex (optional)
    sort = 'sort_example' # str | Return list of branches sorted by the given field (optional)
    page_token = 'page_token_example' # str | Name of branch to start the pagination from (optional)

    try:
        api_response = api_instance.get_api_v4_projects_id_repository_branches(id, page=page, per_page=per_page, search=search, regex=regex, sort=sort, page_token=page_token)
        print("The response of BranchesApi->get_api_v4_projects_id_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->get_api_v4_projects_id_repository_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **page** | **int**| Current page number | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 20]
 **search** | **str**| Return list of branches matching the search criteria | [optional] 
 **regex** | **str**| Return list of branches matching the regex | [optional] 
 **sort** | **str**| Return list of branches sorted by the given field | [optional] 
 **page_token** | **str**| Name of branch to start the pagination from | [optional] 

### Return type

[**List[APIEntitiesBranch]**](APIEntitiesBranch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a project repository branches |  -  |
**404** | 404 Project Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_projects_id_repository_branches_branch**
> APIEntitiesBranch get_api_v4_projects_id_repository_branches_branch(id, branch)



Get a single repository branch

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_branch import APIEntitiesBranch
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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    branch = 56 # int | 

    try:
        api_response = api_instance.get_api_v4_projects_id_repository_branches_branch(id, branch)
        print("The response of BranchesApi->get_api_v4_projects_id_repository_branches_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->get_api_v4_projects_id_repository_branches_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **branch** | **int**|  | 

### Return type

[**APIEntitiesBranch**](APIEntitiesBranch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a single repository branch |  -  |
**404** | Branch Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_api_v4_projects_id_repository_branches_branch**
> head_api_v4_projects_id_repository_branches_branch(id, branch)



Check if a branch exists

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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    branch = 'branch_example' # str | The name of the branch

    try:
        api_instance.head_api_v4_projects_id_repository_branches_branch(id, branch)
    except Exception as e:
        print("Exception when calling BranchesApi->head_api_v4_projects_id_repository_branches_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **branch** | **str**| The name of the branch | 

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
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_projects_id_repository_branches**
> APIEntitiesBranch post_api_v4_projects_id_repository_branches(id, branch, ref)



Create branch

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_branch import APIEntitiesBranch
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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    branch = 'branch_example' # str | The name of the branch
    ref = 'ref_example' # str | Create branch from commit sha or existing branch

    try:
        api_response = api_instance.post_api_v4_projects_id_repository_branches(id, branch, ref)
        print("The response of BranchesApi->post_api_v4_projects_id_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->post_api_v4_projects_id_repository_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **branch** | **str**| The name of the branch | 
 **ref** | **str**| Create branch from commit sha or existing branch | 

### Return type

[**APIEntitiesBranch**](APIEntitiesBranch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create branch |  -  |
**400** | Failed to create branch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_projects_id_repository_branches_branch_protect**
> APIEntitiesBranch put_api_v4_projects_id_repository_branches_branch_protect(id, branch, put_api_v4_projects_id_repository_branches_branch_protect_request=put_api_v4_projects_id_repository_branches_branch_protect_request)



Protect a single branch

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_branch import APIEntitiesBranch
from openapi_client.models.put_api_v4_projects_id_repository_branches_branch_protect_request import PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest
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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    branch = 'branch_example' # str | The name of the branch
    put_api_v4_projects_id_repository_branches_branch_protect_request = openapi_client.PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest() # PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest |  (optional)

    try:
        api_response = api_instance.put_api_v4_projects_id_repository_branches_branch_protect(id, branch, put_api_v4_projects_id_repository_branches_branch_protect_request=put_api_v4_projects_id_repository_branches_branch_protect_request)
        print("The response of BranchesApi->put_api_v4_projects_id_repository_branches_branch_protect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->put_api_v4_projects_id_repository_branches_branch_protect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **branch** | **str**| The name of the branch | 
 **put_api_v4_projects_id_repository_branches_branch_protect_request** | [**PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest**](PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest.md)|  | [optional] 

### Return type

[**APIEntitiesBranch**](APIEntitiesBranch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Protect a single branch |  -  |
**404** | 404 Branch Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_projects_id_repository_branches_branch_unprotect**
> APIEntitiesBranch put_api_v4_projects_id_repository_branches_branch_unprotect(id, branch)



Unprotect a single branch

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_branch import APIEntitiesBranch
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
    api_instance = openapi_client.BranchesApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    branch = 'branch_example' # str | The name of the branch

    try:
        api_response = api_instance.put_api_v4_projects_id_repository_branches_branch_unprotect(id, branch)
        print("The response of BranchesApi->put_api_v4_projects_id_repository_branches_branch_unprotect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->put_api_v4_projects_id_repository_branches_branch_unprotect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **branch** | **str**| The name of the branch | 

### Return type

[**APIEntitiesBranch**](APIEntitiesBranch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unprotect a single branch |  -  |
**404** | 404 Project Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

