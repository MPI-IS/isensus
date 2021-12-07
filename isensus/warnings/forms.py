import typing
import functools
from ..data.user import User
from . decorators import ldap





@ldap
def form_not_sent(user : User) -> str:
    if not user.forms_sent:
        return "ldap is set but the IT forms have not been sent to the user"
    return None

@ldap
def no_mail_account_or_forwarder(user : User) -> str:
    if not (user.mail_account or user.forwarder):
        return "ldap is set but the user has not mail account or forwader"
    return None

@ldap
def no_title(user: User)->str:
    if not user.title:
        return "ldap is set but the user's title has not been set"
    return None

@ldap
def no_contract_type(user: User)->str:
    if not user.contract:
        return "ldap is set but the user's contract type has not been set"
    return None

@ldap
def no_contract_end(user: User)->str:
    if not user.contract:
        return "ldap is set but the user's contract end date has not been set"
    return None
