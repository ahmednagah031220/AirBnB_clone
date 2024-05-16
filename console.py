#!/usr/bin/python3
"""Console of the Project"""
import sys
import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel


def parse(arg):
    return shlex.split(arg)


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ''
    file = None
    __classes = {
        "BaseModel",
    }

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Method used to customize the help message of the Quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        """Method used to customize the message of the EOF help"""
        print("EOF command to exit the program")

    def emptyline(self):
        """Condititonal method used while their are no args"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
