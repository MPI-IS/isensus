import typing
import functools
from ..data.user import User

def not_attr(*attributes : typing.List[str]):
    def _not_attr(f: typing.Callable[[User],str])->typing.Callable[[User],str]:
        def _f(user: User)->str:
            if any([not getattr(user,attr)
                    for attr in attributes]):
                return None
            return f(user)
        return _f
    return _not_attr
    
ldap = functools.partial(_not_attr,"ldap")
""" decorator that ensures None is returned if the ldap attribute is False"""
