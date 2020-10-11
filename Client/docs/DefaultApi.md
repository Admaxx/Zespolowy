# swagger_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/Czacha/Calc/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a_b_op_get**](DefaultApi.md#a_b_op_get) | **GET** /{a}/{b}/{op} | 
[**root_get**](DefaultApi.md#root_get) | **GET** / | 
[**root_post**](DefaultApi.md#root_post) | **POST** / | 


# **a_b_op_get**
> Result a_b_op_get(a, b, op)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
a = 'a_example' # str | 
b = 'b_example' # str | 
op = 'op_example' # str | 

try:
    api_response = api_instance.a_b_op_get(a, b, op)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->a_b_op_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a** | **str**|  | 
 **b** | **str**|  | 
 **op** | **str**|  | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> Result root_get(op=op, a=a, b=b)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
op = 'op_example' # str |  (optional)
a = 'a_example' # str |  (optional)
b = 'b_example' # str |  (optional)

try:
    api_response = api_instance.root_get(op=op, a=a, b=b)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->root_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **op** | **str**|  | [optional] 
 **a** | **str**|  | [optional] 
 **b** | **str**|  | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_post**
> Result root_post(input)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
input = swagger_client.Input() # Input | 

try:
    api_response = api_instance.root_post(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->root_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**Input**](Input.md)|  | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

