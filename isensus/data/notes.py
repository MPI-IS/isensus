from .list_attribute import ListAttribute


class Notes(ListAttribute):

    """ List of notes related to the user

    The end-user may want to attach some (string) notes
    to a user. These notes are stored in the 'notes'
    attribute of the User, which should be an instance of 
    Notes (subclass of ListAttribute).

    Parameters
    ----------
    notes: str
        all notes attached to the users, as a singlue 
        string using '<br>' as separator.
    """

    def __init__(self, notes: str):
        super().__init__(notes)
