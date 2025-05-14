# aind_labtracks_service_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subject**](DefaultApi.md#get_subject) | **GET** /subject/{subject_id} | Get Subject


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
    subject_id = 'subject_id_example' # str | 

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

