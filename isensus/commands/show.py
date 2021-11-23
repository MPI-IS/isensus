from pathlib import Path
from isensus.data.data import Data
from isensus.data.user import User
from isensus.defaults import default_path


def show(usertip: str, path: Path = default_path) -> User:

    """ Print all the value of all attributes of a specific user

    Reads data from the json file, find the user
    corresponding to the usertip, and print the 
    related attributes values.

    Parameters
    ----------
    usertip: str
        First letters of the user's userid, lastname or firstname
    path: Path (optional)
        absolute path to datafile (default to ~/.isensus)

    Returns
    -------
    user: User
        Instance of the updated user after update

    """

    with Data(path=path) as users:
        user = User.find_user(users, usertip)

    print(user.to_string())
    return user
