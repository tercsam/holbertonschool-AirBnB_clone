#!/usr/bin/python3
"""
This is the console module
"""

import cmd

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class defining the commands and functionalities of
    the custom command interpreter.
    Use "help" to get a list of the commands.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """A method to handle an empty command (which is ignored)"""
        pass

    def do_quit(self, arg):
        """quit command, to exit the program"""
        return True

    def do_EOF(self, arg):
        """Recognizes EOF and exits the program"""
        return True

    def do_create(self, arg):
        """
        Creates a new instance from the given class string (arg),
        saves it (to the JSON file) and prints its id.

        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in globals():
            print("** class doesn't exist **")
            return

        cls = globals()[arg]
        new_instance = cls()

        storage.save()

        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        its class name and id.

        Ex: $ show BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()

        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(arg_list) != 2:
            print("** instance id missing **")
            return

        instance_key = f"{arg_list[0]}.{arg_list[1]}"

        if instance_key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[instance_key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()

        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(arg_list) != 2:
            print("** instance id missing **")
            return

        instance_key = f"{arg_list[0]}.{arg_list[1]}"

        if instance_key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[instance_key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.

        Examples:
            $ all BaseModel
            $ all
        """
        if not arg:
            print([str(storage.all()[key]) for key in storage.all()])
            return

        if arg not in globals():
            print("** class doesn't exist **")
            return

        instance_list = []
        for instance_key in storage.all():
            if arg in instance_key:
                instance_list.append(str(storage.all()[instance_key]))

        print(instance_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute (also saves the change into the JSON file).
        Only one attribute can be updated at a time.

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Ex: $ update BaseModel 1234-1234-1234 email "airbnb@mail.com"
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()

        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{arg_list[0]}.{arg_list[1]}"

        if instance_key not in storage.all():
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        setattr(storage.all()[instance_key],
                arg_list[2], arg_list[3].strip('"'))
        storage.save()
        # NOTE A string argument with a space must be between double quotes


if __name__ == '__main__':
    HBNBCommand().cmdloop()
