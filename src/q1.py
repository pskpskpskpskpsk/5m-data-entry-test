def swap_values(x, y):
    """
    Swaps the values of x and y without using a temporary variable.

    Args:
        x: The first value.
        y: The second value.

    Returns:
        -1 if x or y is not a numeric type (int or float), otherwise prints the swapped values.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    else:
        x = x + y
        y = x - y
        x = x - y
        print(f"The swapped values are x = {x} and y = {y}")
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
