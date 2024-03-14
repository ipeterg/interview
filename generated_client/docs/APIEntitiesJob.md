# APIEntitiesJob

API_Entities_Job model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the job | [optional] 
**name** | **str** | The name of the job | [optional] 
**status** | **str** | The current status of the job | [optional] 
**stage** | **str** | The stage of the job in the CI/CD pipeline | [optional] 
**created_at** | **datetime** | The creation time of the job | [optional] 
**started_at** | **datetime** | The start time of the job | [optional] 
**finished_at** | **datetime** | The finish time of the job | [optional] 
**commit** | [**APIEntitiesCommit**](APIEntitiesCommit.md) |  | [optional] 
**archived** | **bool** | Indicates if the job is archived | [optional] 
**allow_failure** | **bool** | Indicates if the job is allowed to fail | [optional] 
**erased_at** | **datetime** | The time when the job was erased, if applicable | [optional] 
**duration** | **int** | The duration of the job in seconds | [optional] 
**queued_duration** | **float** | The duration the job was queued before execution, in seconds | [optional] 
**ref** | **str** | The reference for the job | [optional] 
**artifacts** | **List[object]** | The artifacts produced by the job | [optional] 
**tag** | **bool** | Indicates if the job is tagged | [optional] 
**web_url** | **str** | The URL for accessing the job in the web interface | [optional] 
**project** | [**APIEntitiesJobProject**](APIEntitiesJobProject.md) |  | [optional] 
**user** | [**APIEntitiesUserBasic**](APIEntitiesUserBasic.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_job import APIEntitiesJob

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesJob from a JSON string
api_entities_job_instance = APIEntitiesJob.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesJob.to_json())

# convert the object into a dict
api_entities_job_dict = api_entities_job_instance.to_dict()
# create an instance of APIEntitiesJob from a dict
api_entities_job_form_dict = api_entities_job.from_dict(api_entities_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


