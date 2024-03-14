# openapi_client.AdminApi

All URIs are relative to *https://www.gitlab.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v4_admin_databases_database_name_dictionary_tables_table_name**](AdminApi.md#get_api_v4_admin_databases_database_name_dictionary_tables_table_name) | **GET** /api/v4/admin/databases/{database_name}/dictionary/tables/{table_name} | 


# **get_api_v4_admin_databases_database_name_dictionary_tables_table_name**
> APIEntitiesDictionaryTable get_api_v4_admin_databases_database_name_dictionary_tables_table_name(database_name, table_name)



Retrieve dictionary details

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_entities_dictionary_table import APIEntitiesDictionaryTable
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
    api_instance = openapi_client.AdminApi(api_client)
    database_name = 'database_name_example' # str | The database name
    table_name = 'table_name_example' # str | The table name

    try:
        api_response = api_instance.get_api_v4_admin_databases_database_name_dictionary_tables_table_name(database_name, table_name)
        print("The response of AdminApi->get_api_v4_admin_databases_database_name_dictionary_tables_table_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_api_v4_admin_databases_database_name_dictionary_tables_table_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_name** | **str**| The database name | 
 **table_name** | **str**| The table name | 

### Return type

[**APIEntitiesDictionaryTable**](APIEntitiesDictionaryTable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve dictionary details |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

