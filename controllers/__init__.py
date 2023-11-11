def boolFromQuery(q: str) -> bool:
    """
    Interpets query parameter as a bool.

    Args:
        q (str): query paramter

    Returns:
        bool: `True` for "true" and "1", `False` otherwise. Case insensitive.
    """
    if q is None:
        return False

    if q.isdigit():
        if q == "1":
            return True
        return False

    if q.lower() == "true":
        return True
    return False
