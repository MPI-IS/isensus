import typing

from .list import list
from .rm import rm
from .create import create
from .set import set
from .show import show
from .delnote import delnote
from .delwarning import delwarning

"""
Dictionary having as values all the commands that
the end-user may perform on the database of users.
"""
commands: typing.Dict[str, typing.Callable] = {
    "list": list,
    "delnote": delnote,
    "delwarning": delwarning,
    "create": create,
    "set": set,
    "show": show,
}
