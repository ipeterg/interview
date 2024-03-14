# openapi_client.PlanLimitsApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v4_application_plan_limits**](PlanLimitsApi.md#get_api_v4_application_plan_limits) | **GET** /api/v4/application/plan_limits | Get current plan limits
[**put_api_v4_application_plan_limits**](PlanLimitsApi.md#put_api_v4_application_plan_limits) | **PUT** /api/v4/application/plan_limits | Change plan limits


# **get_api_v4_application_plan_limits**
> APIEntitiesPlanLimit get_api_v4_application_plan_limits(plan_name=plan_name)

Get current plan limits

List the current limits of a plan on the GitLab instance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_plan_limit import APIEntitiesPlanLimit
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
    api_instance = openapi_client.PlanLimitsApi(api_client)
    plan_name = 'default' # str | Name of the plan to get the limits from. Default: default. (optional) (default to 'default')

    try:
        # Get current plan limits
        api_response = api_instance.get_api_v4_application_plan_limits(plan_name=plan_name)
        print("The response of PlanLimitsApi->get_api_v4_application_plan_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanLimitsApi->get_api_v4_application_plan_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_name** | **str**| Name of the plan to get the limits from. Default: default. | [optional] [default to &#39;default&#39;]

### Return type

[**APIEntitiesPlanLimit**](APIEntitiesPlanLimit.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current plan limits |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_application_plan_limits**
> APIEntitiesPlanLimit put_api_v4_application_plan_limits(put_api_v4_application_plan_limits_request)

Change plan limits

Modify the limits of a plan on the GitLab instance.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_plan_limit import APIEntitiesPlanLimit
from openapi_client.models.put_api_v4_application_plan_limits_request import PutApiV4ApplicationPlanLimitsRequest
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
    api_instance = openapi_client.PlanLimitsApi(api_client)
    put_api_v4_application_plan_limits_request = openapi_client.PutApiV4ApplicationPlanLimitsRequest() # PutApiV4ApplicationPlanLimitsRequest | 

    try:
        # Change plan limits
        api_response = api_instance.put_api_v4_application_plan_limits(put_api_v4_application_plan_limits_request)
        print("The response of PlanLimitsApi->put_api_v4_application_plan_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanLimitsApi->put_api_v4_application_plan_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_api_v4_application_plan_limits_request** | [**PutApiV4ApplicationPlanLimitsRequest**](PutApiV4ApplicationPlanLimitsRequest.md)|  | 

### Return type

[**APIEntitiesPlanLimit**](APIEntitiesPlanLimit.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Change plan limits |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

