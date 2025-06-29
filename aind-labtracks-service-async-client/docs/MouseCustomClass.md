# MouseCustomClass

Schema for MouseCustomClass that will be parsed from XML

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserved_by** | **str** |  | [optional] 
**reserved_date** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**full_genotype** | **str** |  | [optional] 
**phenotype** | **str** |  | [optional] 

## Example

```python
from aind_labtracks_service_async_client.models.mouse_custom_class import MouseCustomClass

# TODO update the JSON string below
json = "{}"
# create an instance of MouseCustomClass from a JSON string
mouse_custom_class_instance = MouseCustomClass.from_json(json)
# print the JSON string representation of the object
print(MouseCustomClass.to_json())

# convert the object into a dict
mouse_custom_class_dict = mouse_custom_class_instance.to_dict()
# create an instance of MouseCustomClass from a dict
mouse_custom_class_from_dict = MouseCustomClass.from_dict(mouse_custom_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


