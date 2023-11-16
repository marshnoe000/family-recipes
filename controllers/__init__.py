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
        return q == "1"

    return q.lower() == "true"
