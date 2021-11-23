from .list_attribute import ListAttribute


class Warnings(ListAttribute):

    """ List of warnings related to the user

    The end-user may want to attach some (string) warnings
    to a user. These warnings are stored in the 'warnings'
    attribute of the User, which should be an instance of 
    Warnings (subclass of ListAttribute).

    Parameters
    ----------
    warnings: str
        all warnings attached to the users, as a singlue 
        string using '<br>' as separator.
    """

    def __init__(self, warnings: str):
        super().__init__(warnings)
