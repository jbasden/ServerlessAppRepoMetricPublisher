import json
import requests

import boto3 #for the client
import uuid  #for unique logStream names
import time

CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000


def validator(event):
    """Checks the user input to make sure all necessary information is present,
    attempts to convert everything to the proper type, and returns an error
    message if unsuccessful.

    Parameters:
        event (dict) : contains the user input

    Returns:
        (str): message of validation
    """

    if "Namespace" not in event or event["Namespace"]  == "":
        return "Invalid Namespace"
    event["Namespace"] = str(event["Namespace"])
    if "MetricName" not in event or event["MetricName"] == "":
        return "Invalid MetricName"
    event["MetricName"] = str(event["MetricName"])
    if "Dimensions" in event:
        for dimension in event["Dimensions"]:
            if "Name" not in dimension or dimension["Name"] == "":
                return "Invalid Dimension Name"
            dimension["Name"] = str(dimension["Name"])
            if "Value" not in dimension or dimension["Value"] == "":
                return "Invalid Dimension Value"
            dimension["Value"] = str(dimension["Value"])
    if "Timestamp" in event:
        try:
            event["Timestamp"] = int(event["Timestamp"])
        except ValueError:
            return "Timestamp must be an integer (epoch format)."
    if "Value" in event:
        try:
            event["Value"] = float(event["Value"])
        except ValueError:
            return "Value type must be float."
    if "StatisticValues" in event:
        if "SampleCount" not in event["StatisticValues"]:
            return "Statistic Values require a Sample Count."
        try:
            event["StatisticValues"]["SampleCount"] = float(event["StatisticValues"]["SampleCount"])
        except ValueError:
            return "Invalid SampleCount"
        if "Sum" not in event["StatisticValues"]:
            return "Statistic Values require a Sum."
        try:
            event["StatisticValues"]["Sum"] = float(event["StatisticValues"]["Sum"])
        except ValueError:
            return "Invalid Sum"
        if "Minimum" not in event["StatisticValues"]:
            return "Statistic Values require a Minimum."
        try:
            event["StatisticValues"]["Minimum"] = float(event["StatisticValues"]["Minimum"])
        except ValueError:
            return "Invalid Minimum"
        if "Maximum" not in event["StatisticValues"]:
            return "Statistic Values require a Maximum."
        try:
            event["StatisticValues"]["Maximum"] = float(event["StatisticValues"]["Maximum"])
        except ValueError:
            return "Invalid Maximum"
        if event["StatisticValues"]["Minimum"] > event["StatisticValues"]["Maximum"]:
            return "Minimum cannot be greater than Maximum."
    if "Unit" in event:
        event["Unit"] = str(event["Unit"])
        possibleUnits = ['Seconds','Microseconds','Milliseconds','Bytes',\
            'Kilobytes','Megabytes','Gigabytes','Terabytes','Bits','Kilobits',\
            'Megabits','Gigabits','Terabits','Percent','Count','Bytes/Second',\
            'Kilobytes/Second','Megabytes/Second','Gigabytes/Second',\
            'Terabytes/Second','Bits/Second','Kilobits/Second','Megabits/Second',\
            'Gigabits/Second','Terabits/Second','Count/Second','None']
        if event["Unit"] not in possibleUnits:
            return "Unit type not available"
    if "StorageResolution" in event:
        try:
            event["StorageResolution"] = int(event["StorageResolution"])
        except ValueError:
            return "StorageResolution type must be integer."
    return "Validated"

def formMessage(event):
    """Forms the message with the proper syntax given the user input,
    including only those values provided by the user.

    Parameters:
        event (dict): the user input

    Returns:
        message (dict): the message with the correct format
    """

    message = {
        "Namespace": event["Namespace"],
        "MetricData": [
            {
                "MetricName": event["MetricName"]
            },
        ]
    }
    if "Dimensions" in event:
        message["MetricData"][0]["Dimensions"] = event["Dimensions"]
    if "Timestamp" in event:
        message["MetricData"][0]["Timestamp"] = event["Timestamp"]
    if "Value" in event:
        message["MetricData"][0]["Value"] = event["Value"]
    if "StatisticValues" in event:
        message["MetricData"][0]["StatisticValues"] = event["StatisticValues"]
    if "Unit" in event:
        message["MetricData"][0]["Unit"] = event["Unit"]
    if "StorageResolution" in event:
        message["MetricData"][0]["StorageResolution"] = event["StorageResolution"]
    return message

def metricLogger(message):
    """Puts the user input message into a newly created log stream.

    Parameters:
        message (dict): the message to put to the log stream

    Returns:
        None
    """
    client = boto3.client('logs',region_name="us-east-1")
    message = str(message)
    newUUID = str(uuid.uuid4())
    newLogStreamName = 'metricPublisherAppLogStream-' + newUUID
    client.create_log_stream(logGroupName='metricPublisherAppLogGroup', logStreamName=newLogStreamName)
    client.put_log_events(
        logGroupName='metricPublisherAppLogGroup',
        logStreamName=newLogStreamName,
        logEvents=[
            {
                'timestamp': int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR),
                'message': message
            },
        ],
    )

def lambda_handler_provided(event, context):
    """Sample pure Lambda function

    Arguments:
        event LambdaEvent -- Lambda Event received from Invoke API
        context LambdaContext -- Lambda Context runtime methods and attributes

    Returns:
        dict -- {'statusCode': int, 'body': dict}
    """


    ip = requests.get('http://checkip.amazonaws.com/')

    return {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'hello world',
            'location': ip.text.replace('\n', ''),
        })
    }

def lambda_handler(event, context):
    """Handler function for the metricLogger Lambda function.

    Parameters:
        event (dict): the user input

    Returns:
        (str) message upon successful execution
    """

    validatorMessage = validator(event)
    if validatorMessage != "Validated":
        return validatorMessage
    message = formMessage(event)
    #metricLogger(message)
    return "Function executed through to completion."
