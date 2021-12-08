import inspect
import typing
import functools
from ..data.user import User

class IWarning:
    """
    Base class for warnings. An instance of IWarning must have a __call__ method
    which takes an instance of isensus.Data.User as argument and returns None
    if not warning, a string describing the warning otherwise.
    """
    
    def __call__(self, user: User)->str:
        raise NotImplementedError("subclasses of isensus.IWarning must implement "
                                  "a __call__ method [[User],str]")

class BoolsWarning(IWarning):
    """
    Subclass of IWarning which will return a warning if all "the attributes"
    of the user are True, and all the "not_attributes" of the user
    are False.
    """
    
    def __init__(self, attributes: typing.Sequence[str],not_attributes: typing.Sequence[str]):
        self._attributes = attributes
        self._not_attributes = not_attributes

    def _get_warning_message(self)->str:
        def _get_grammar(attrs):
            if len(attrs)==1:
                return [attrs[0],
                        "attribute",
                        "is"]
            return [", ".join(attrs),
                    "attributes",
                    "are"]
        attr_grammar = _get_grammar(self._attributes)
        not_attr_grammar = _get_grammar(self._not_attributes)
        formats = attr_grammar + not_attr_grammar
        return str("{} {} {} True, "
                   "but {} {} {} not".format(*formats))
        
    def __call__(self, user: User)->str:
        if any([not getattr(user,attr) for
                attr in self._attributes]):
            return None
        if any([getattr(user,attr)
                for attr in self._not_attributes]):
            return None
        return self._get_warning_message()
    
form_not_sent = BoolsWarning(["ldap"],["forms_sent"])
""" Warning if ldap is True but froms_sent is None or False"""

no_mail_account_or_forwarder = BoolsWarning(["ldap"],["mail_account","forwarder"])
""" Warning if ldap is True but neither mail_account nor fowarder is True"""

no_title = BoolsWarning(["ldap"],["title"])
""" Warning if ldap is True but title is None"""

no_contract_type = BoolsWarning(["ldap"],["contract"])
""" Warning if ldap is true but contract is None"""

no_contract_end = BoolsWarning(["ldap"],["contract_end"])
""" Warning if ldap is True but contract_end is None"""

# creating a convenience list containing all warning classes
_var = None
_locs = locals()
warnings : typing.Tuple[IWarning] = tuple([_var for _var in _locs.values()
                                           if inspect.isclass(_var)
                                           and issubclass(_var,IWarning)])
""" Tuple containing all the warning classes"""
