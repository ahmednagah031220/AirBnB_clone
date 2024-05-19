#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import json
import re
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname, method, args = match.groups()
        match_uid_and_args = re.search(r'^"([^"]*)"(?:, (.*))?$', args)
        uid, attr_or_dict = match_uid_and_args.groups() \
            if match_uid_and_args else (args, None)

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search(r'^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                r'^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(1) or "") + \
                    " " + (match_attr_and_value.group(2) or "")
        command = f"{method} {classname} {uid} {attr_and_value}"
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for each, value in d.items():
                    if each in attributes:
                        value = attributes[each](value)
                    setattr(storage.all()[key], each, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates an instance."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{words[0]}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{words[0]}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances."""
        if line:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in storage.all().values()
                       if type(obj).__name__ == words[0]])
        else:
            print([str(obj) for obj in storage.all().values()])

    def do_count(self, line):
        """Counts the instances of a class."""
        words = line.split(' ')
        var = len([k for k in storage.all() if k.startswith(words[0] + '.')])
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            print(var)

    def do_update(self, line):
        """Updates an instance by adding or updating each."""
        if not line:
            print("** class name missing **")
            return

        match = re.search(
            r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:\S+)))?)?)?',
            line)
        if not match:
            print("** class name missing **")
            return
        classname, uid, each, value = match.groups()
        if classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            elif not each:
                print("** each name missing **")
            elif not value:
                print("** value missing **")
            else:
                if not re.search('^".*"$', value):
                    value = float(value) if '.' in value else int(value)
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if each in attributes:
                    value = attributes[each](value)
                setattr(storage.all()[key], each, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
