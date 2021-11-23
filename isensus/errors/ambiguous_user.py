import typing


class AmbiguousUserError(Exception):
    """ Raised when one user is searched in the data but several users are found.
    
    Parameters
    ----------
    usertip: str
        End-user search string, corresponding to the first letters of either
        the userid, the first name or the last name of the user.
    candidates: list of str
        List of userids of users corresponding to the search string.
    """

    def __init__(self, usertip: str, candidates: typing.Sequence[str]):
        self._tip = tip
        self._candidates = ", ".join(candidates)

    def __str__(self):
        return str(
            "ambiguous user: {}, "
            "can correspond to: {}".format(self._tip, self._candidates)
        )
