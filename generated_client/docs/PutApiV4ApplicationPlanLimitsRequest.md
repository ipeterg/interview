# PutApiV4ApplicationPlanLimitsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_name** | **str** | Name of the plan to update | 
**ci_pipeline_size** | **int** | Maximum number of jobs in a single pipeline | [optional] 
**ci_active_jobs** | **int** | Total number of jobs in currently active pipelines | [optional] 
**ci_project_subscriptions** | **int** | Maximum number of pipeline subscriptions to and from a project | [optional] 
**ci_pipeline_schedules** | **int** | Maximum number of pipeline schedules | [optional] 
**ci_needs_size_limit** | **int** | Maximum number of DAG dependencies that a job can have | [optional] 
**ci_registered_group_runners** | **int** | Maximum number of runners registered per group | [optional] 
**ci_registered_project_runners** | **int** | Maximum number of runners registered per project | [optional] 
**conan_max_file_size** | **int** | Maximum Conan package file size in bytes | [optional] 
**enforcement_limit** | **int** | Maximum storage size for the root namespace enforcement in MiB | [optional] 
**generic_packages_max_file_size** | **int** | Maximum generic package file size in bytes | [optional] 
**helm_max_file_size** | **int** | Maximum Helm chart file size in bytes | [optional] 
**maven_max_file_size** | **int** | Maximum Maven package file size in bytes | [optional] 
**notification_limit** | **int** | Maximum storage size for the root namespace notifications in MiB | [optional] 
**npm_max_file_size** | **int** | Maximum NPM package file size in bytes | [optional] 
**nuget_max_file_size** | **int** | Maximum NuGet package file size in bytes | [optional] 
**pypi_max_file_size** | **int** | Maximum PyPI package file size in bytes | [optional] 
**terraform_module_max_file_size** | **int** | Maximum Terraform Module package file size in bytes | [optional] 
**storage_size_limit** | **int** | Maximum storage size for the root namespace in MiB | [optional] 
**pipeline_hierarchy_size** | **int** | Maximum number of downstream pipelines in a pipeline&#39;s hierarchy tree | [optional] 

## Example

```python
from openapi_client.models.put_api_v4_application_plan_limits_request import PutApiV4ApplicationPlanLimitsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutApiV4ApplicationPlanLimitsRequest from a JSON string
put_api_v4_application_plan_limits_request_instance = PutApiV4ApplicationPlanLimitsRequest.from_json(json)
# print the JSON string representation of the object
print(PutApiV4ApplicationPlanLimitsRequest.to_json())

# convert the object into a dict
put_api_v4_application_plan_limits_request_dict = put_api_v4_application_plan_limits_request_instance.to_dict()
# create an instance of PutApiV4ApplicationPlanLimitsRequest from a dict
put_api_v4_application_plan_limits_request_form_dict = put_api_v4_application_plan_limits_request.from_dict(put_api_v4_application_plan_limits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


