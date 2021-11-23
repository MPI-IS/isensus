class UserNotFoundError(Exception):
    """ Raised when an user is not found in the data.

    Parameters
    ----------
    userid: str
        The userid key that is not part of the database.
    """

    def __init__(self, userid: str):
        self._userid = userid

    def __str__(self):
        return "unknown user: {}".format(self._userid)
