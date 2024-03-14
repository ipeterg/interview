# openapi_client.JobsApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_single_job**](JobsApi.md#get_single_job) | **GET** /api/v4/projects/{id}/jobs/{job_id} | Get a single job by ID
[**list_project_jobs**](JobsApi.md#list_project_jobs) | **GET** /api/v4/projects/{id}/jobs | List jobs for a project
[**trigger_manual_job**](JobsApi.md#trigger_manual_job) | **POST** /api/v4/projects/{id}/jobs/{job_id}/play | Run a manual job


# **get_single_job**
> APIEntitiesJob get_single_job(id, job_id)

Get a single job by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_job import APIEntitiesJob
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
    api_instance = openapi_client.JobsApi(api_client)
    id = 56 # int | The ID of the project
    job_id = 56 # int | The ID of the job

    try:
        # Get a single job by ID
        api_response = api_instance.get_single_job(id, job_id)
        print("The response of JobsApi->get_single_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_single_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the project | 
 **job_id** | **int**| The ID of the job | 

### Return type

[**APIEntitiesJob**](APIEntitiesJob.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single job object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_jobs**
> List[APIEntitiesJob] list_project_jobs(id, scope=scope)

List jobs for a project

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_job import APIEntitiesJob
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
    api_instance = openapi_client.JobsApi(api_client)
    id = 56 # int | The ID of the project
    scope = ['scope_example'] # List[str] | Return all jobs with the specified statuses (optional)

    try:
        # List jobs for a project
        api_response = api_instance.list_project_jobs(id, scope=scope)
        print("The response of JobsApi->list_project_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_project_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the project | 
 **scope** | [**List[str]**](str.md)| Return all jobs with the specified statuses | [optional] 

### Return type

[**List[APIEntitiesJob]**](APIEntitiesJob.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_manual_job**
> trigger_manual_job(id, job_id, job_variables_attributes=job_variables_attributes)

Run a manual job

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
    api_instance = openapi_client.JobsApi(api_client)
    id = 56 # int | The ID of the project
    job_id = 56 # int | The ID of the manual job to run
    job_variables_attributes = ['job_variables_attributes_example'] # List[str] | An array containing the custom variables available to the job (optional)

    try:
        # Run a manual job
        api_instance.trigger_manual_job(id, job_id, job_variables_attributes=job_variables_attributes)
    except Exception as e:
        print("Exception when calling JobsApi->trigger_manual_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the project | 
 **job_id** | **int**| The ID of the manual job to run | 
 **job_variables_attributes** | [**List[str]**](str.md)| An array containing the custom variables available to the job | [optional] 

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
**200** | Job started successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

