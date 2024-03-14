# openapi_client.AlertManagementApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id**](AlertManagementApi.md#delete_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id) | **DELETE** /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/{metric_image_id} | 
[**get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images**](AlertManagementApi.md#get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images) | **GET** /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images | 
[**post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images**](AlertManagementApi.md#post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images) | **POST** /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images | 
[**post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_authorize**](AlertManagementApi.md#post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_authorize) | **POST** /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/authorize | 
[**put_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id**](AlertManagementApi.md#put_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id) | **PUT** /api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/{metric_image_id} | 


# **delete_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id**
> APIEntitiesMetricImage delete_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id(id, alert_iid, metric_image_id)



Remove a metric image for an alert

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_metric_image import APIEntitiesMetricImage
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
    api_instance = openapi_client.AlertManagementApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    alert_iid = 56 # int | The IID of the Alert
    metric_image_id = 56 # int | The ID of metric image

    try:
        api_response = api_instance.delete_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id(id, alert_iid, metric_image_id)
        print("The response of AlertManagementApi->delete_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertManagementApi->delete_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **alert_iid** | **int**| The IID of the Alert | 
 **metric_image_id** | **int**| The ID of metric image | 

### Return type

[**APIEntitiesMetricImage**](APIEntitiesMetricImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Remove a metric image for an alert |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images**
> List[APIEntitiesMetricImage] get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images(id, alert_iid)



Metric Images for alert

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_metric_image import APIEntitiesMetricImage
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
    api_instance = openapi_client.AlertManagementApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    alert_iid = 56 # int | The IID of the Alert

    try:
        api_response = api_instance.get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images(id, alert_iid)
        print("The response of AlertManagementApi->get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertManagementApi->get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **alert_iid** | **int**| The IID of the Alert | 

### Return type

[**List[APIEntitiesMetricImage]**](APIEntitiesMetricImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metric Images for alert |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images**
> APIEntitiesMetricImage post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images(id, alert_iid, file, url=url, url_text=url_text)



Upload a metric image for an alert

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_metric_image import APIEntitiesMetricImage
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
    api_instance = openapi_client.AlertManagementApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    alert_iid = 56 # int | The IID of the Alert
    file = None # bytearray | The image file to be uploaded
    url = 'url_example' # str | The url to view more metric info (optional)
    url_text = 'url_text_example' # str | A description of the image or URL (optional)

    try:
        api_response = api_instance.post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images(id, alert_iid, file, url=url, url_text=url_text)
        print("The response of AlertManagementApi->post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertManagementApi->post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **alert_iid** | **int**| The IID of the Alert | 
 **file** | **bytearray**| The image file to be uploaded | 
 **url** | **str**| The url to view more metric info | [optional] 
 **url_text** | **str**| A description of the image or URL | [optional] 

### Return type

[**APIEntitiesMetricImage**](APIEntitiesMetricImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload a metric image for an alert |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_authorize**
> post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_authorize(id, alert_iid)



Workhorse authorize metric image file upload

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
    api_instance = openapi_client.AlertManagementApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    alert_iid = 56 # int | The IID of the Alert

    try:
        api_instance.post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_authorize(id, alert_iid)
    except Exception as e:
        print("Exception when calling AlertManagementApi->post_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **alert_iid** | **int**| The IID of the Alert | 

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
**200** | Workhorse authorize metric image file upload |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id**
> APIEntitiesMetricImage put_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id(id, alert_iid, metric_image_id, url=url, url_text=url_text)



Update a metric image for an alert

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_metric_image import APIEntitiesMetricImage
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
    api_instance = openapi_client.AlertManagementApi(api_client)
    id = 'id_example' # str | The ID or URL-encoded path of the project
    alert_iid = 56 # int | The IID of the Alert
    metric_image_id = 56 # int | The ID of metric image
    url = 'url_example' # str | The url to view more metric info (optional)
    url_text = 'url_text_example' # str | A description of the image or URL (optional)

    try:
        api_response = api_instance.put_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id(id, alert_iid, metric_image_id, url=url, url_text=url_text)
        print("The response of AlertManagementApi->put_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertManagementApi->put_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or URL-encoded path of the project | 
 **alert_iid** | **int**| The IID of the Alert | 
 **metric_image_id** | **int**| The ID of metric image | 
 **url** | **str**| The url to view more metric info | [optional] 
 **url_text** | **str**| A description of the image or URL | [optional] 

### Return type

[**APIEntitiesMetricImage**](APIEntitiesMetricImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a metric image for an alert |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

