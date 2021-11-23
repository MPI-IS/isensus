class ExistingUserError(Exception):
    """ Raised when the user attempts to create
    a new user using an already existing userid.

    Parameters
    ----------
    userid: str
        The userid key that is already in the 
        database.
    """

    def __init__(self, userid: str):
        self._userid = userid

    def __str__(self):
        return "userid {} already exists".format(self._userid)
