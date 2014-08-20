def parse_and_validate_port(portString):
    """Parses and validates a port number from a string.

    Attempts to parse an integer from the provided string. If an integer can 
    be parsed, the value is validated to check if it falls in the range 1024 
    to 65535 inclusive.

    Args:
        portString: A string 

    Returns:
        The port number as an integer. If a valid port number could not be 
        parsed, the return value will be None.
    """
    try:
        port = int(portString)
        if port < 1024 or port > 65535:
            return None

        return port

    except ValueError: 
        return None