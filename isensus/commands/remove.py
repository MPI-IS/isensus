from pathlib import Path
from ..data import Data
from ..default import default_path


def remove(usertip: str, path: Path = default_path) -> object:
    """ Removes a user from the database.

    Reads data from the json file, find the corresponding
    user and removes it from the data.

    Parameters
    ----------
    usertip: str
        First letters of the user's userid, lastname or firstname
    path: Path (optional)
        absolute path to datafile (default to ~/.isensus)

    Returns
    -------
    user: User
        Instance of the removed user
    """

    with Data(path=path) as users:
        user = User.find_user(users, usertip)
        del users[user.userid]

    return user
