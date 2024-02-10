#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
        implement a class that inherits from the cmd class
        and has a prompt "hbnb"
    """

    prompt = "(hbnb) "

    def do_emptyline(self):
        """
            this method does nothing\n
        """
        pass
    def do_quit(self, arg):
        """Quit command to exit the program.\n"""

        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program.\n"""

        return True

    def create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """



if __name__ == "__main__":
    HBNBCommand().cmdloop()
