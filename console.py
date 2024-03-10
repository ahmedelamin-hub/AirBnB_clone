#!/usr/bin/python3
"""
HBNBCommand class for the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        args = split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] in self.__class_dict:
            instance = self.__class_dict[args[0]]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Shows the string representation of an instance based on the class name and id."""
        args = split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] in self.__class_dict:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] in self.__class_dict:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        args = split(line)
        if args and args[0] not in self.__class_dict:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        obj_list = []
        for obj_id, obj in all_objs.items():
            if not args or args[0] == obj.__class__.__name__:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] in self.__class_dict:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            obj = storage.all()[key]
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
