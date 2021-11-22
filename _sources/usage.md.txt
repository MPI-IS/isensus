# Usage

## under construction

isensus is currently under development, and you should not expect the functionality
described in this file to work correctly.

## json data

isensus is a wrapper over a user database encoded in a json formated file.

This file is located in `~/.isensus`, and isensus will create it automatically if
it does not exists.

## executable

### commands

The isensus executable supports these commands:

- list: print the list of users
- create: create a new user. Arguments:
  - the userid (unique identifier in the database)
  - the first name (without spaces)
  - the last name (without spaces)
- set: set the value of a user attribute. Arguments:
  - usertip : the first letters of either the userid, the first name or the last name of the user
  - attribute: the attribute to update
  - value: the value the attribute should be set to
- delnote: delete a note of the "notes" attribute. Argmuments:
  - usertip : the first letters of either the userid, the first name or the last name of the user
  - index of the note to delete
- delwarning: delete a warning of the "warnings" attribute. Argmuments:
  - usertip : the first letters of either the userid, the first name or the last name of the user
  - index of the warning to delete
- show: print the user's attribute. Arguments:
  - usertip : the first letters of either the userid, the first name or the last name of the user

### automatic warnings

(upcoming)