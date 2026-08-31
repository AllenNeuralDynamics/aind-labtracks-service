# aind_labtracks_service_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subject**](DefaultApi.md#get_subject) | **GET** /subject/{subject_id} | Get Subject
[**get_subject_by_protocol_number**](DefaultApi.md#get_subject_by_protocol_number) | **GET** /subject_by_protocol_number/{protocol_number} | Get Subject By Protocol Number
[**get_tasks**](DefaultApi.md#get_tasks) | **GET** /tasks/{subject_id} | Get Tasks


# **get_subject**
> List[Subject] get_subject(subject_id)

Get Subject

## Subject metadata
Retrieves subject information from LabTracks.

### Example


```python
import aind_labtracks_service_client
from aind_labtracks_service_client.models.subject import Subject
from aind_labtracks_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_labtracks_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_labtracks_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_labtracks_service_client.DefaultApi(api_client)
    subject_id = '632269' # str | 

    try:
        # Get Subject
        api_response = api_instance.get_subject(subject_id)
        print("The response of DefaultApi->get_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | 

### Return type

[**List[Subject]**](Subject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subject_by_protocol_number**
> List[Subject] get_subject_by_protocol_number(protocol_number)

Get Subject By Protocol Number

## Subject metadata
Retrieves subject information from LabTracks.

### Example


```python
import aind_labtracks_service_client
from aind_labtracks_service_client.models.subject import Subject
from aind_labtracks_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_labtracks_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_labtracks_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_labtracks_service_client.DefaultApi(api_client)
    protocol_number = '0401' # str | 

    try:
        # Get Subject By Protocol Number
        api_response = api_instance.get_subject_by_protocol_number(protocol_number)
        print("The response of DefaultApi->get_subject_by_protocol_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_subject_by_protocol_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_number** | **str**|  | 

### Return type

[**List[Subject]**](Subject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> List[Task] get_tasks(subject_id)

Get Tasks

## Task metadata
Retrieves Task information from LabTracks.

### Example


```python
import aind_labtracks_service_client
from aind_labtracks_service_client.models.task import Task
from aind_labtracks_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_labtracks_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_labtracks_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_labtracks_service_client.DefaultApi(api_client)
    subject_id = '632269' # str | 

    try:
        # Get Tasks
        api_response = api_instance.get_tasks(subject_id)
        print("The response of DefaultApi->get_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

