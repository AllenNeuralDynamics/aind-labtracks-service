# Subject

Expected Subject view of joined tables

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**class_values** | [**MouseCustomClass**](MouseCustomClass.md) |  | [optional] 
**sex** | **str** |  | [optional] 
**birth_date** | **datetime** |  | [optional] 
**species_name** | **str** |  | [optional] 
**cage_id** | **str** |  | [optional] 
**room_id** | **str** |  | [optional] 
**paternal_id** | **str** |  | [optional] 
**paternal_class_values** | [**MouseCustomClass**](MouseCustomClass.md) |  | [optional] 
**maternal_id** | **str** |  | [optional] 
**maternal_class_values** | [**MouseCustomClass**](MouseCustomClass.md) |  | [optional] 
**group_name** | **str** |  | [optional] 
**group_description** | **str** |  | [optional] 

## Example

```python
from aind_labtracks_service_client.models.subject import Subject

# TODO update the JSON string below
json = "{}"
# create an instance of Subject from a JSON string
subject_instance = Subject.from_json(json)
# print the JSON string representation of the object
print(Subject.to_json())

# convert the object into a dict
subject_dict = subject_instance.to_dict()
# create an instance of Subject from a dict
subject_from_dict = Subject.from_dict(subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


