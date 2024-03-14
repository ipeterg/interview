# APIEntitiesPlanLimit

API_Entities_PlanLimit model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ci_pipeline_size** | **int** |  | [optional] 
**ci_active_jobs** | **int** |  | [optional] 
**ci_project_subscriptions** | **int** |  | [optional] 
**ci_pipeline_schedules** | **int** |  | [optional] 
**ci_needs_size_limit** | **int** |  | [optional] 
**ci_registered_group_runners** | **int** |  | [optional] 
**ci_registered_project_runners** | **int** |  | [optional] 
**conan_max_file_size** | **int** |  | [optional] 
**enforcement_limit** | **int** |  | [optional] 
**generic_packages_max_file_size** | **int** |  | [optional] 
**helm_max_file_size** | **int** |  | [optional] 
**limits_history** | **object** |  | [optional] 
**maven_max_file_size** | **int** |  | [optional] 
**notification_limit** | **int** |  | [optional] 
**npm_max_file_size** | **int** |  | [optional] 
**nuget_max_file_size** | **int** |  | [optional] 
**pipeline_hierarchy_size** | **int** |  | [optional] 
**pypi_max_file_size** | **int** |  | [optional] 
**terraform_module_max_file_size** | **int** |  | [optional] 
**storage_size_limit** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_plan_limit import APIEntitiesPlanLimit

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesPlanLimit from a JSON string
api_entities_plan_limit_instance = APIEntitiesPlanLimit.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesPlanLimit.to_json())

# convert the object into a dict
api_entities_plan_limit_dict = api_entities_plan_limit_instance.to_dict()
# create an instance of APIEntitiesPlanLimit from a dict
api_entities_plan_limit_form_dict = api_entities_plan_limit.from_dict(api_entities_plan_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


