from pathlib import Path
from isensus.defaults import default_path
from isensus.data.data import Data


def list(path: Path = default_path) -> None:
    """ Print the list of users included in the database

    Parameters
    ----------
    path: Path (optional)
        absolute path to datafile (default to ~/.isensus)
    """

    with Data(path=path) as users:
        attrs = ("firstname", "lastname")
        userids = sorted(users.keys())
        for userid, user in users.item():
            values = [getattr(user, attr) for attr in attrs]
            print(userid, "\t", "\t".join(values))
