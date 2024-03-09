#!/usr/bin/python3
"""Defines the HBNB command interpreter."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""
    prompt = '(hbnb) '
    __classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Doesn't execute anything on empty line input."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        # Implementation of create command
        
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""
        # Implementation of show command
        
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        # Implementation of destroy command
        
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        # Implementation of all command
        
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        # Implementation of update command

if __name__ == '__main__':
    HBNBCommand().cmdloop()
