from pathlib import Path
from isensus.data.notes import Notes
from isensus.data.warnings import Warnings
from isensus.data.list_attribute import ListAttribute
from isensus.data.data import Data
from isensus.data.user import User
from isensus.defaults import default_path


def set(usertip: str, attribute: str, value: str, path: Path = default_path) -> User:
    """ Set a users's attribute value
    
    Reads the data from the json file, find the user corresponding
    to the usertip, and set the attribute of the user to the 
    given value (after casting to proper type). May raise
    various exception (e.g. ValueError, UserNotFoundError, etc).
    The attributes warnings and notes are a bit special: the value
    is added to the attribute (and not set to the attribute).

    Parameters
    ----------
    usertip: str
        First letters of the user's userid, lastname or firstname
    attribute: str
        name of the attribute to update
    value: str
        string representation of the value the attribute should take 
    path: Path (optional)
        absolute path to datafile (default to ~/.isensus)

    Returns
    -------
    user: User
        Instance of the updated user after update
    """

    with Data(path=path) as users:
        user = User.find_user(users, usertip)
        attr_type = User.get_type(attribute)
        if not attr_type in (Notes,Warnings):
            setattr(user, attribute, attr_type(value))
            return
        # attribute is warnings or notes :
        # adding the value to the already existing
        # values
        current = repr(getattr(user, attribute))
        if not current:
            new_value = value
        else:
            new_value = current + ListAttribute.separator + value
        setattr(user, attribute, new_value)
        
    return user
