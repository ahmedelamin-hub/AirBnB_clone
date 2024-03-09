#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from uuid import uuid4
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel(str(uuid4()))
            print(new_instance.id)
            # Here, you should implement saving the instance to a file
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows the details of a BaseModel instance based on its id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        # Implement logic to show instance based on its id

    def do_destroy(self, arg):
        """Destroys a BaseModel instance based on its id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        # Implement logic to destroy instance based on its id

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name."""
        # Implement logic to print all instances or instances of a specific class

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = shlex.split(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
