# PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developers_can_push** | **bool** | Flag if developers can push to that branch | [optional] 
**developers_can_merge** | **bool** | Flag if developers can merge to that branch | [optional] 

## Example

```python
from openapi_client.models.put_api_v4_projects_id_repository_branches_branch_protect_request import PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest from a JSON string
put_api_v4_projects_id_repository_branches_branch_protect_request_instance = PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest.from_json(json)
# print the JSON string representation of the object
print(PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest.to_json())

# convert the object into a dict
put_api_v4_projects_id_repository_branches_branch_protect_request_dict = put_api_v4_projects_id_repository_branches_branch_protect_request_instance.to_dict()
# create an instance of PutApiV4ProjectsIdRepositoryBranchesBranchProtectRequest from a dict
put_api_v4_projects_id_repository_branches_branch_protect_request_form_dict = put_api_v4_projects_id_repository_branches_branch_protect_request.from_dict(put_api_v4_projects_id_repository_branches_branch_protect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


