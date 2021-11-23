import typing
from pathlib import Path
from isensus.data.data import Data
from isensus.data.user import User
from isensus.defaults import default_path

# the rm method accepts only these two attributes
WarningsOrNotes = typing.Literal["warnings", "notes"]
warnings_or_notes_g = ("warnings", "notes")


def rm(
    usertip: str, attribute: WarningsOrNotes, index: int, path: Path = default_path
) -> User:
    """  Remove a user's warning or note
    
    Reads the data from the json file and find the user corresponding
    to the usertip. Then remove the entry corresponding to 
    the attribute (warnings or note) at the given index.
    Return the instance of User that has been updated.

    Parameters
    ----------
    usertip: str
        First letters of the user's userid, lastname or firstname
    attribute: str
        should be of the value "warnings" or "notes"
    index: int
        index of warnings or the notes to remove
    path: Path (optional)
        absolute path to datafile (default to ~/.isensus)

    Returns
    -------
    user: User
        Instance of the updated user after update
    """
    with Data(path=path) as users:
        user = User.find_user(users)
        if attribute not in warnings_or_note_g:
            raise UnexpectedAttributeError(attribute, warnings_or_notes_g)
        getattr(user, attribute).rm(index)

    return user
