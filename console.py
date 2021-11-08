#!/usr/bin/python3
"""inicializer console"""
import cmd
import datetime
import json
from models import storage
from models.base_model import BaseModel
import shlex

class_name = {'BaseModel': BaseModel}

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

    def do_create(self, args):
        """ Creates a new instance """
        if not (args):
            print("** class name missing **")
        elif args not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        else:
            instance = eval[args]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ Prints str representation"""
        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in class_name:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if args[1] == v.id:
                        print(v)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in class_name:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """ Prints all str representation of all instances """
        split_args = shlex.split(args)
        n_list = []
        dict_json = models.storage.all()
        if args:
            try:
                for key in models.storage.all():
                    if split_args[0] == key.split('.')[0]:
                        n_list.append(str(dict_json[key]))
                print(n_list)
            except Exception:
                print("** class doesn't exist **")
        else:
            for key in models.storage.all():
                n_list.append(str(models.storage.all()[key]))
            print(n_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_name:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
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
