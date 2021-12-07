import typing
import functools
from ..data.user import User

def _not_attr(attribute: str, f: typing.Callable[[User],str])->typing.Callable[[User],str]:
    """
    Decorator tool that ensures the function returns None
    if  the specified attribute of the user is False.
    """
    def _f(user: User)->str:
        if not user.ldap:
            return None
        return f(user)
    return _f

ldap = functools.partial(_not_attr,"ldap")
""" decorator that ensures None is returned if the ldap attribute is False"""
