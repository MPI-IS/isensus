""" Path the default json database file
"""

import json, typing
from pathlib import Path
from .user import User
from ..defaults import default_path


def get_data(path: Path) -> typing.Dict[str, User]:
    """ Read the json file database

    Reads the json data file (~/.isensus by default) and
    return the corresponding instances of User.

    Parameters
    ----------
    path: Path 
      Absolute path to the json file database 

    Returns
    -------
    users: dict
        userids (str) as keys, instances of User as
        values.
    """
    json_content = _read_json_file(path)
    return User.from_json(json_content)


def write_data(users: typing.Dict[str, User], path: Path) -> None:
    """
    Writes the users in the json data file
    (~/.isensus).

    Parameters
    ----------
    users: dict
      Dictionary of users to encode and write to the file.
      keys: userid (str), values: instance of User.
    path: Path
      Absolute path to the json database file (will be 
      overwritten if exists)
    """
    json_content = User.to_json(users)
    with open(path, "w") as f:
        f.write(json_content)


def _read_json_file(path: Path) -> typing.Dict[str, str]:
    # Attempt to parse the file provided by the path,
    # returning a (json serialized) dict or raising a
    # FileNotFoundError or a ValueError
    if not path.is_file():
        raise FileNotFoundError(
            "failed to find isensus " "data file: {}".format(json_path)
        )
    try:
        with open(path) as f:
            data = json.load(f)
    except Exception as e:
        raise ValueError(
            "failed to parse isensus json " "data file {}: {}".format(path, e)
        )
    return data


class Data:
    """ Context manager for json database file.

    Context manager that will read the data json file
    (~/.isensus) when entering, returning the 
    corresponding dictionary {userid: instance of User}.
    At exit, this dictionary is written back in the data
    file. Hence, the returned dictionary is mutabled, and
    users are expected to modify it.

    Parameters
    ----------
    path: Path (optional)
      Absolute path to the json file database.
      Defaults to ~/.isensus
    """

    def __init__(self, path: default_path):
        self._path = path

    def __enter__(self) -> typing.Dict[str, User]:
        self._users = get_data(self._path)
        return self._users

    def __exit__(self, type, value, traceback):
        write_data(self._users, self._path)
