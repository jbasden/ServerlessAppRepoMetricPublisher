"""Lambda function entrypoint handlers."""


def log_event(event, context):
    """Log event.

    Parameters:
        event (dict): the user input

    Returns:
        (str) message upon successful execution

    """
    return "Function executed through to completion."
