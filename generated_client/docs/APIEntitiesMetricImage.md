# APIEntitiesMetricImage

API_Entities_MetricImage model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**filename** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_entities_metric_image import APIEntitiesMetricImage

# TODO update the JSON string below
json = "{}"
# create an instance of APIEntitiesMetricImage from a JSON string
api_entities_metric_image_instance = APIEntitiesMetricImage.from_json(json)
# print the JSON string representation of the object
print(APIEntitiesMetricImage.to_json())

# convert the object into a dict
api_entities_metric_image_dict = api_entities_metric_image_instance.to_dict()
# create an instance of APIEntitiesMetricImage from a dict
api_entities_metric_image_form_dict = api_entities_metric_image.from_dict(api_entities_metric_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


