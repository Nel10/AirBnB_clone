#!/usr/bin/python3
"""inicializer console"""
import cmd
import datetime
import json
import models
from models.base_model import BaseModel
from models.user import User
import shlex

class_name = {'BaseModel': BaseModel, 'User': User}


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """End of File"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """dont execute nothing"""
        pass

    def do_create(self, args):
        """ Creates a new instance """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_name:
            instance = class_name[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, args):
        """ Prints str representation"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_name:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Deletes an instance"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_name:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """ Prints all stri representation of all instances """
        args = shlex.split(args)
        n_list = []
        if len(args) == 0:
            for valu in models.storage.all().values():
                n_list.append(str(valu))
                print("[", end="")
                print(",".join(n_list), end="")
                print("]")
        elif args[0] in class_name:
            for key in models.storage.all():
                if args[0] in key:
                    n_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(n_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_name:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[key], args[2],
                                    args[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
