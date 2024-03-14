# APIEntitiesCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**short_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**parent_ids** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_email** | **str** |  | [optional] 
**authored_date** | **datetime** |  | [optional] 
**committer_name** | **str** |  | [optional] 
**committer_email** | **str** |  | [optional] 
**committed_date** | **datetime** |  | [optional] 
**trailers** | **object** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_commit import APIEntitiesCommit

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesCommit from a JSON string
api_entities_commit_instance = APIEntitiesCommit.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesCommit.to_json())

# convert the object into a dict
api_entities_commit_dict = api_entities_commit_instance.to_dict()
# create an instance of APIEntitiesCommit from a dict
api_entities_commit_form_dict = api_entities_commit.from_dict(api_entities_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


