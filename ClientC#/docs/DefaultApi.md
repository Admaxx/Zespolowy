# IO.Swagger.Api.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/Czacha/Calc/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ABOpGet**](DefaultApi.md#abopget) | **GET** /{a}/{b}/{op} | 
[**RootGet**](DefaultApi.md#rootget) | **GET** / | 
[**RootPost**](DefaultApi.md#rootpost) | **POST** / | 


<a name="abopget"></a>
# **ABOpGet**
> Result ABOpGet (string a, string b, string op)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ABOpGetExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var a = a_example;  // string | 
            var b = b_example;  // string | 
            var op = op_example;  // string | 

            try
            {
                Result result = apiInstance.ABOpGet(a, b, op);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.ABOpGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a** | **string**|  | 
 **b** | **string**|  | 
 **op** | **string**|  | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="rootget"></a>
# **RootGet**
> Result RootGet (string op = null, string a = null, string b = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class RootGetExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var op = op_example;  // string |  (optional) 
            var a = a_example;  // string |  (optional) 
            var b = b_example;  // string |  (optional) 

            try
            {
                Result result = apiInstance.RootGet(op, a, b);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.RootGet: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **op** | **string**|  | [optional] 
 **a** | **string**|  | [optional] 
 **b** | **string**|  | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="rootpost"></a>
# **RootPost**
> Result RootPost (Input input)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class RootPostExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var input = new Input(); // Input | 

            try
            {
                Result result = apiInstance.RootPost(input);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.RootPost: " + e.Message );
            }
        }
    }
}
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

