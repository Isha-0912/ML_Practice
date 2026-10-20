def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    if value is None:
        return False
    if value==0:
        return False
    if isinstance(value,(str,tuple,list,set,dict)) and len(value)==0:
        return False
    return True

def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for item in values:
        if is_truthy(item):
            return item
    return None
