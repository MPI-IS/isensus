class UnknownAttributeError(Exception):
    """ Raised when the user attemps to attribute
    a non supported attribute.

    Parameters
    ----------
    attribute: str
        Name of the non supported attribute.
    """

    def __init__(self, attribute: str):
        self._attribute = attribute

    def __str__(self):
        return "Unknown attribute: {}".format(self._attribute)
