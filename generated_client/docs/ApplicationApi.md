# openapi_client.ApplicationApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v4_application_appearance**](ApplicationApi.md#get_api_v4_application_appearance) | **GET** /api/v4/application/appearance | 
[**put_api_v4_application_appearance**](ApplicationApi.md#put_api_v4_application_appearance) | **PUT** /api/v4/application/appearance | 


# **get_api_v4_application_appearance**
> APIEntitiesAppearance get_api_v4_application_appearance()



Get the current appearance

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_appearance import APIEntitiesAppearance
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
    api_instance = openapi_client.ApplicationApi(api_client)

    try:
        api_response = api_instance.get_api_v4_application_appearance()
        print("The response of ApplicationApi->get_api_v4_application_appearance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->get_api_v4_application_appearance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIEntitiesAppearance**](APIEntitiesAppearance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the current appearance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_api_v4_application_appearance**
> APIEntitiesAppearance put_api_v4_application_appearance(title=title, description=description, pwa_name=pwa_name, pwa_short_name=pwa_short_name, pwa_description=pwa_description, logo=logo, pwa_icon=pwa_icon, header_logo=header_logo, favicon=favicon, new_project_guidelines=new_project_guidelines, profile_image_guidelines=profile_image_guidelines, header_message=header_message, footer_message=footer_message, message_background_color=message_background_color, message_font_color=message_font_color, email_header_and_footer_enabled=email_header_and_footer_enabled)



Modify appearance

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_appearance import APIEntitiesAppearance
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
    api_instance = openapi_client.ApplicationApi(api_client)
    title = 'title_example' # str | Instance title on the sign in / sign up page (optional)
    description = 'description_example' # str | Markdown text shown on the sign in / sign up page (optional)
    pwa_name = 'pwa_name_example' # str | Name of the Progressive Web App (optional)
    pwa_short_name = 'pwa_short_name_example' # str | Optional, short name for Progressive Web App (optional)
    pwa_description = 'pwa_description_example' # str | An explanation of what the Progressive Web App does (optional)
    logo = None # bytearray | Instance image used on the sign in / sign up page (optional)
    pwa_icon = None # bytearray | Icon used for Progressive Web App (optional)
    header_logo = None # bytearray | Instance image used for the main navigation bar (optional)
    favicon = None # bytearray | Instance favicon in .ico/.png format (optional)
    new_project_guidelines = 'new_project_guidelines_example' # str | Markdown text shown on the new project page (optional)
    profile_image_guidelines = 'profile_image_guidelines_example' # str | Markdown text shown on the profile page below Public Avatar (optional)
    header_message = 'header_message_example' # str | Message within the system header bar (optional)
    footer_message = 'footer_message_example' # str | Message within the system footer bar (optional)
    message_background_color = 'message_background_color_example' # str | Background color for the system header / footer bar (optional)
    message_font_color = 'message_font_color_example' # str | Font color for the system header / footer bar (optional)
    email_header_and_footer_enabled = True # bool | Add header and footer to all outgoing emails if enabled (optional)

    try:
        api_response = api_instance.put_api_v4_application_appearance(title=title, description=description, pwa_name=pwa_name, pwa_short_name=pwa_short_name, pwa_description=pwa_description, logo=logo, pwa_icon=pwa_icon, header_logo=header_logo, favicon=favicon, new_project_guidelines=new_project_guidelines, profile_image_guidelines=profile_image_guidelines, header_message=header_message, footer_message=footer_message, message_background_color=message_background_color, message_font_color=message_font_color, email_header_and_footer_enabled=email_header_and_footer_enabled)
        print("The response of ApplicationApi->put_api_v4_application_appearance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->put_api_v4_application_appearance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Instance title on the sign in / sign up page | [optional] 
 **description** | **str**| Markdown text shown on the sign in / sign up page | [optional] 
 **pwa_name** | **str**| Name of the Progressive Web App | [optional] 
 **pwa_short_name** | **str**| Optional, short name for Progressive Web App | [optional] 
 **pwa_description** | **str**| An explanation of what the Progressive Web App does | [optional] 
 **logo** | **bytearray**| Instance image used on the sign in / sign up page | [optional] 
 **pwa_icon** | **bytearray**| Icon used for Progressive Web App | [optional] 
 **header_logo** | **bytearray**| Instance image used for the main navigation bar | [optional] 
 **favicon** | **bytearray**| Instance favicon in .ico/.png format | [optional] 
 **new_project_guidelines** | **str**| Markdown text shown on the new project page | [optional] 
 **profile_image_guidelines** | **str**| Markdown text shown on the profile page below Public Avatar | [optional] 
 **header_message** | **str**| Message within the system header bar | [optional] 
 **footer_message** | **str**| Message within the system footer bar | [optional] 
 **message_background_color** | **str**| Background color for the system header / footer bar | [optional] 
 **message_font_color** | **str**| Font color for the system header / footer bar | [optional] 
 **email_header_and_footer_enabled** | **bool**| Add header and footer to all outgoing emails if enabled | [optional] 

### Return type

[**APIEntitiesAppearance**](APIEntitiesAppearance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modify appearance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

