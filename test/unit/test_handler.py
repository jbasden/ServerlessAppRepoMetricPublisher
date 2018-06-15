import json
import pytest
import events
from jsonschema import ValidationError
import metricpublisher.schema
import metricpublisher.lambda_handler

def test_standard_valid_input():
    data = events.standard_valid_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_basic_valid_input():
    data = events.basic_valid_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_multiple_metrics_input():
    data = events.multiple_metrics_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_Value_and_Statistic_Values_both_included():
    data = events.value_and_statistic_values_both_included()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_value_and_statistic_values():
    data = events.missing_value_and_statistic_values()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_request_id():
    data = events.missing_request_id()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_metric_name():
    data = events.missing_metric_name()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_StatisticValues_missing_Sum():
    data = events.StatisticValues_missing_Sum()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_Unit_type_not_available():
    data = events.Unit_type_not_available()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_StorageResolution_type_invalid():
    data = events.StorageResolution_type_invalid()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def _assert_error_response(result, error_type):
    assert 'error' in result
    assert 'type' in result['error']
    assert result['error']['type'] == error_type
