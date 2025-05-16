# Task

Expected Task view of joined tables

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type_name** | **str** |  | [optional] 
**date_start** | **datetime** |  | [optional] 
**date_end** | **datetime** |  | [optional] 
**investigator_id** | **str** |  | [optional] 
**task_description** | **str** |  | [optional] 
**task_object** | **str** |  | [optional] 
**protocol_number** | **str** |  | [optional] 
**protocol_title** | **str** |  | [optional] 
**task_status** | **str** |  | [optional] 

## Example

```python
from aind_labtracks_service_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


