import json
import pytest
import events
from jsonschema import ValidationError
import metricpublisher.schema
import metricpublisher.lambda_handler

def test_standard_valid_input():
    """Test to make sure a standard valid input passes the JSON schema"""
    data = events.standard_valid_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_basic_valid_input():
    """Test to make sure a minimalistic input passes the JSON schema"""
    data = events.basic_valid_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_multiple_metrics_input():
    """Test to validate that the option to input multiple metrics simultaneously is available."""
    data = events.multiple_metrics_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_Value_and_Statistic_Values_both_included():
    """Test to assert that customer cannot pass in both 'Value' and
    'StatisticValues' in the input. (They are mutually exclusive)."""
    data = events.value_and_statistic_values_both_included()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_value_and_statistic_values():
    """Test to make sure at least one of 'Value' or 'StatisticValues' is present"""
    data = events.missing_value_and_statistic_values()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_request_id():
    """Test to make sure a request_id is passed in by the customer"""
    data = events.missing_request_id()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_metric_name():
    """Test to make sure a metric name is passed in by the customer"""
    data = events.missing_metric_name()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_StatisticValues_missing_Sum():
    """Test to make sure that 'Sum' is present when 'StatisticValues' is"""
    data = events.StatisticValues_missing_Sum()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_Unit_type_not_available():
    """Test to make sure that customer must pass in a valid unit type"""
    data = events.Unit_type_not_available()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_StorageResolution_type_invalid():
    """Test to make sure the input type of 'StorageResolution' is valid"""
    data = events.StorageResolution_type_invalid()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_dimension_type_invalid():
    """Test to make sure the input type of 'Dimension' is valid"""
    data = events.Dimension_type_invalid ()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def _assert_error_response(result, error_type):
    """Helper function to assert that the correct type of error was thrown"""
    assert 'error' in result
    assert 'type' in result['error']
    assert result['error']['type'] == error_type
