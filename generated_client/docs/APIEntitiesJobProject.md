# APIEntitiesJobProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ci_job_token_scope_enabled** | **bool** | Indicates if the CI/CD job token scope setting is enabled for the project | [optional] 

## Example

```python
from openapi_client.models.api_entities_job_project import APIEntitiesJobProject

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesJobProject from a JSON string
api_entities_job_project_instance = APIEntitiesJobProject.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesJobProject.to_json())

# convert the object into a dict
api_entities_job_project_dict = api_entities_job_project_instance.to_dict()
# create an instance of APIEntitiesJobProject from a dict
api_entities_job_project_form_dict = api_entities_job_project.from_dict(api_entities_job_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


