class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class QuantityGreaterThanItemQuantity(Error):
    """ Trying to remove item from cart but quantity is greater """
    pass
