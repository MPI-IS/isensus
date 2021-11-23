"""
isensus executable. see: https://mpi-is.github.io/isensus/
"""

import sys, inspect
from isensus.commands import commands


def _list_commands():
    """
    List the commands along with their arguments
    """

    print()
    for command in commands.values():
        args = inspect.getfullargspec(command).args
        if not args:
            print(command.__name__, ": (no arguments)")
        else:
            types = command.__annotations__
            arg_types = [str(arg) + " (" + str(types[arg]) + ")" for arg in args]
            print(command.__name__, ":", " ".join(arg_types))
    print()


def _run(args):

    # user did not pass any commands. Printing documentation
    if not args:
        _list_commands()
        return

    # user passed an unknown command. Printing documentation
    if args[0] not in commands.keys():
        print("\nUnknown command: {}".format(args[0]))
        _list_commands()
        return

    # the command the user want to execute
    command = commands[args[0]]
    # the arguments as provided by the user
    user_args = args[1:]

    # correct number of arguments ?
    nb_args = len(inspect.getfullargspec(command).args)

    # incorrect number of argument
    if nb_args != len(args[1:]):
        print("\nIncorrect number of argument")
        _list_commands()
        return

    # are the arguments provided by the user of the
    # suitable type ?
    command_args = inspect.getfullargspec(command).args
    input_args = []
    for user_arg, command_arg in zip(user_args, command_args):
        try:
            # casting user argument (str) to type expected by
            # the command's function
            input_arg = command.__annotations__[command_args](user_arg)
        except Exception as e:
            # casting failed, exiting
            print(
                "\nfailed to cast argument {} to {}".format(
                    user_arg, command.__annotations__[command_args]
                )
            )
            print()
            return
        input_args.append(input_arg)

    # applying the command
    user = command(*input_args)

    # if a user is returned by the command, this means this user
    # has been updated. So showing the updated user
    if user:
        commands["list"](user.userid)


def run():

    _run(sys.argv[1:])
