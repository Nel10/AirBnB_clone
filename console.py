#!/usr/bin/python3
"""inicializer console"""
import cmd
import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """End Of File"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """dont execute nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
