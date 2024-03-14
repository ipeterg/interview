# APIEntitiesDictionaryTable

API_Entities_Dictionary_Table model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** |  | [optional] 
**feature_categories** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_dictionary_table import APIEntitiesDictionaryTable

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesDictionaryTable from a JSON string
api_entities_dictionary_table_instance = APIEntitiesDictionaryTable.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesDictionaryTable.to_json())

# convert the object into a dict
api_entities_dictionary_table_dict = api_entities_dictionary_table_instance.to_dict()
# create an instance of APIEntitiesDictionaryTable from a dict
api_entities_dictionary_table_form_dict = api_entities_dictionary_table.from_dict(api_entities_dictionary_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


