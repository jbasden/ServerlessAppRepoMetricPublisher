"""Collection of events for schema validation"""
import pytest

@pytest.fixture()
def standard_valid_input():
    return {
        "request_id": "an id",
        "metric_data": [
            {
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
                "StatisticValues": {
                    "SampleCount": 12.17,
                    "Sum": 12.17,
                    "Minimum": 12.17,
                    "Maximum": 12.17
                },
                "Unit": "Seconds",
                "StorageResolution": 12
            }
        ]
    }

@pytest.fixture()
def basic_valid_input():
    return {
        "request_id":"an id",
        "metric_data": [
            {
                "MetricName": "theMetricName",
                "Value":123,
            }
        ]
    }

@pytest.fixture()
def multiple_metrics_input():
    return {
        "request_id": "an id",
        "metric_data": [
            {
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
                "StatisticValues": {
                    "SampleCount": 12.17,
                    "Sum": 12.17,
                    "Minimum": 12.17,
                    "Maximum": 12.17
                },
                "Unit": "Seconds",
                "StorageResolution": 12
            },
            {
                "MetricName": "theMetricName2",
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
                "Value":123,
                "Unit": "Seconds",
                "StorageResolution": 12
            }
        ]
    }


@pytest.fixture()
def value_and_statistic_values_both_included():
    return {
        "request_id": "an id",
        "metric_data": [
            {
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
                "Value": 123,
                "StatisticValues": {
                    "SampleCount": 12.17,
                    "Sum": 12.17,
                    "Minimum": 12.17,
                    "Maximum": 12.17
                },
                "Unit": "Seconds",
                "StorageResolution": 12
            }
        ]
    }

@pytest.fixture()
def missing_value_and_statistic_values():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "MetricName": "the_metric_name",
                "Dimensions": [
                    {
                        "Name": "the_name_1",
                        "Value": "the_value_1"
                    },
                    {
                        "Name": "the_name_2",
                        "Value": "the_value_2"
                    }
                ],
                "Timestamp": 1528236844480,
                "Unit": "Seconds",
                "StorageResolution": 12
            }
        ]
    }

@pytest.fixture()
def missing_request_id():
    return {
        "metric_data": [
            {
                "MetricName": "the_metric_name",
                "Dimensions": [
                    {
                        "Name": "the_name_1",
                        "Value": "the_value_1"
                    },
                    {
                        "Name": "the_name_2",
                        "Value": "the_value_2"
                    }
                ],
                "Timestamp": 1528236844480,
                "Value":123,
                "Unit": "Seconds",
                "StorageResolution": 12
            }
        ]
    }

@pytest.fixture()
def missing_metric_name():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "Dimensions": [
                    {
                        "Name": "the_name_1",
                        "Value": "the_value_1"
                    },
                    {
                        "Name": "the_name_2",
                        "Value": "the_value_2"
                    }
                ],
                "Timestamp": 1528236844480,
                "Value":123,
                "Unit": "Seconds",
                "StorageResolution": 12
            }
        ]
    }

@pytest.fixture()
def StatisticValues_missing_Sum():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "MetricName": "the_metric_name",
                "Dimensions": [
                    {
                        "Name": "the_name_1",
                        "Value": "the_value_1"
                    },
                    {
                        "Name": "the_name_2",
                        "Value": "the_value_2"
                    }
                ],
                "Timestamp": 1528236844480,
                "StatisticValues": {
                    "SampleCount": 12.17,
                    "Minimum": 12.17,
                    "Maximum": 12.17
                },
                "Unit": "Seconds",
                "StorageResolution": 12
            }
        ]
    }

@pytest.fixture()
def Unit_type_not_available():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "MetricName": "the_metric_name",
                "Dimensions": [
                    {
                        "Name": "the_name_1",
                        "Value": "the_value_1"
                    },
                    {
                        "Name": "the_name_2",
                        "Value": "the_value_2"
                    }
                ],
                "Timestamp": 1528236844480,
                "StatisticValues": {
                    "SampleCount": 12.17,
                    "Sum": 12.17,
                    "Minimum": 12.17,
                    "Maximum": 12.17
                },
                "Unit": "minutes",
                "StorageResolution": 12
            }
        ]
    }

@pytest.fixture()
def StorageResolution_type_invalid():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "MetricName": "the_metric_name",
                "Dimensions": [
                    {
                        "Name": "the_name_1",
                        "Value": "the_value_1"
                    },
                    {
                        "Name": "the_name_2",
                        "Value": "the_value_2"
                    }
                ],
                "Timestamp": 1528236844480,
                "StatisticValues": {
                    "SampleCount": 12.17,
                    "Sum": 12.17,
                    "Minimum": 12.17,
                    "Maximum": 12.17
                },
                "Unit": "Seconds",
                "StorageResolution": "12"
            }
        ]
    }
