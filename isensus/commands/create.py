from pathlib import Path
from isensus.data.data import Data
from isensus.data.user import User
from isensus.errors import ExistingUserError
from isensus.defaults import default_path


def create(
    userid: str, firstname: str, lastname: str, path: Path = default_path
) -> User:

    """ Adds a new user to the database

    Reads the data from the json file and if not user of the same
    userid exists, adds a new instance of User to it (with reasonable
    defaults attributes values)

    Parameters
    ----------
    userid : str
        userid, as entered in ldap
    firstname: str
        first name of the user
    lastname: str
        last name of the user
    path: Path (optional)
        absolute path to datafile (default to ~/.isensus)

    Returns
    -------
    user: User
        Instance corresponding of the added user.
    
    Raises
    ------

    ExistingUserError 
        if a user with the provided userid already exists.
    """

    with Data(path=path) as users:
        if userid in users.keys():
            raise ExistingUserError(userid)
        user: User = User.create_new(userid, firstname, lastname)
        users[userid] = user

    return user
