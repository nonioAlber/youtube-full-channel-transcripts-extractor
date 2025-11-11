thonimport datetime

def get_current_timestamp():
    """Returns the current timestamp in ISO format."""
    return datetime.datetime.now().isoformat()