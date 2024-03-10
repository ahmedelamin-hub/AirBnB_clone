#!/usr/bin/python3
"""
A command interpreter for managing AirBnB clone objects.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from shlex import split
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __class_dict = {
        'BaseModel': BaseModel,
        'User': User,
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.__class_dict:
            print("** class doesn't exist **")
            return
        instance = self.__class_dict[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg and arg not in self.__class_dict:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        print_list = []
        for obj_id in all_objs:
            if not arg or arg == all_objs[obj_id].__class__.__name__:
                print_list.append(str(all_objs[obj_id]))
        print(print_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in all_objs:
            print("** no instance found **")
            return
        setattr(all_objs[key], args[2], args[3])
        all_objs[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
