# openapi_client.MigrationsApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_api_v4_admin_migrations_timestamp_mark**](MigrationsApi.md#post_api_v4_admin_migrations_timestamp_mark) | **POST** /api/v4/admin/migrations/{timestamp}/mark | 


# **post_api_v4_admin_migrations_timestamp_mark**
> post_api_v4_admin_migrations_timestamp_mark(timestamp, put_api_v4_admin_batched_background_migrations_id_resume_request=put_api_v4_admin_batched_background_migrations_id_resume_request)



Mark the migration as successfully executed

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
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
    api_instance = openapi_client.MigrationsApi(api_client)
    timestamp = 56 # int | The migration version timestamp
    put_api_v4_admin_batched_background_migrations_id_resume_request = openapi_client.PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest() # PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest |  (optional)

    try:
        api_instance.post_api_v4_admin_migrations_timestamp_mark(timestamp, put_api_v4_admin_batched_background_migrations_id_resume_request=put_api_v4_admin_batched_background_migrations_id_resume_request)
    except Exception as e:
        print("Exception when calling MigrationsApi->post_api_v4_admin_migrations_timestamp_mark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| The migration version timestamp | 
 **put_api_v4_admin_batched_background_migrations_id_resume_request** | [**PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest**](PutApiV4AdminBatchedBackgroundMigrationsIdResumeRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 Created |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not found |  -  |
**422** | You can mark only pending migrations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

