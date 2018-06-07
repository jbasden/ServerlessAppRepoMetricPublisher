import json
import pytest
from hello_world import app


"""@pytest.fixture()
def apigw_event():
    #Generates API GW Event

    return {
        "body": "{ \"test\": \"body\"}",
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": ""
            },
            "stage": "prod"
        },
        "queryStringParameters": {
            "foo": "bar"
        },
        "headers": {
            "Via":
            "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language":
            "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer":
            "true",
            "CloudFront-Is-SmartTV-Viewer":
            "false",
            "CloudFront-Is-Mobile-Viewer":
            "false",
            "X-Forwarded-For":
            "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country":
            "US",
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests":
            "1",
            "X-Forwarded-Port":
            "443",
            "Host":
            "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto":
            "https",
            "X-Amz-Cf-Id":
            "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer":
            "false",
            "Cache-Control":
            "max-age=0",
            "User-Agent":
            "Custom User Agent String",
            "CloudFront-Forwarded-Proto":
            "https",
            "Accept-Encoding":
            "gzip, deflate, sdch"
        },
        "pathParameters": {
            "proxy": "/examplepath"
        },
        "httpMethod": "POST",
        "stageVariables": {
            "baz": "qux"
        },
        "path": "/examplepath"
    }"""

@pytest.fixture()
def event1():
    return {
        "Namespace": "theNamespace",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "theName1",
                "Value": "theValue1"
            },
            {
                "Name": "theName2",
                "Value": "theValue2"
            }
        ],
        "Timestamp": 1528236844480,
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event2():
    return {
        "Namespace": "basicNamespace",
        "MetricName": "basicMetricName"
    }

@pytest.fixture()
def event3():
    return {
        "Namespace": "",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "theName1",
                "Value": "theValue1"
            },
            {
                "Name": "theName2",
                "Value": "theValue2"
            }
        ],
        "Timestamp": 1528236844480,
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event4():
    return {
        "Namespace": "theNamespace",
        "MetricName": "",
        "Dimensions": [
            {
                "Name": "theName1",
                "Value": "theValue1"
            },
            {
                "Name": "theName2",
                "Value": "theValue2"
            }
        ],
        "Timestamp": 1528236844480,
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event5():
    return {
        "Namespace": "theNamespace",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "",
                "Value": "theValue"
            }
        ],
        "Timestamp": 1528236844480,
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event6():
    return {
        "Namespace": "theNamespace",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "theName",
                "Value": ""
            }
        ],
        "Timestamp": 1528236844480,
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event7():
    return {
        "Namespace": "theNamespace",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "theName",
                "Value": "theValue"
            }
        ],
        "Timestamp": "Fake time stamp",
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event8():
    return {
        "Namespace": "theNamespace",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "theName",
                "Value": "theValue"
            }
        ],
        "Timestamp": "1528319852774",
        "Value": "Fake Value",
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event9():
    return {
        "Namespace": "theNamespace",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "theName",
                "Value": "theValue"
            }
        ],
        "Timestamp": "1528319852774",
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.18,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def event10():
    return {
        "Namespace": "theNamespace",
        "MetricName": "theMetricName",
        "Dimensions": [
            {
                "Name": "theName",
                "Value": "theValue"
            }
        ],
        "Timestamp": "1528319852774",
        "Value": 12.17,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "seconds",
        "StorageResolution": 12
    }

"""
def test_lambda_handler_provided(apigw_event):

    ret = app.lambda_handler_provided(apigw_event, "")
    assert ret['statusCode'] == 200

    for key in ('message', 'location'):
        assert key in ret['body']

    data = json.loads(ret['body'])
    assert data['message'] == 'hello world'
"""

def test_lambda_handler1(event1):
    ret = app.lambda_handler(event1, "")
    assert ret == "Function executed through to completion."

def test_lambda_handler2(event2):
    ret = app.lambda_handler(event2, "")
    assert ret == "Function executed through to completion."

def test_lambda_handler3(event3):
    ret = app.lambda_handler(event3, "")
    assert ret == "Invalid Namespace"

def test_lambda_handler4(event4):
    ret = app.lambda_handler(event4, "")
    assert ret == "Invalid MetricName"

def test_lambda_handler5(event5):
    ret = app.lambda_handler(event5, "")
    assert ret == "Invalid Dimension Name"

def test_lambda_handler6(event6):
    ret = app.lambda_handler(event6, "")
    assert ret == "Invalid Dimension Value"

def test_lambda_handler7(event7):
    ret = app.lambda_handler(event7, "")
    assert ret == "Timestamp must be an integer (epoch format)."

def test_lambda_handler8(event8):
    ret = app.lambda_handler(event8, "")
    assert ret == "Value type must be float."

def test_lambda_handler9(event9):
    ret = app.lambda_handler(event9, "")
    assert ret == "Minimum cannot be greater than Maximum."

def test_lambda_handler10(event10):
    ret = app.lambda_handler(event10, "")
    assert ret == "Unit type not available"
