#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    that contains the entry point of the command interpreter
    """
    
    prompt = "(hbnb) "

    def do_quit(self, x):
        """Quit command to exit the program.\n"""

        return True
    
    def do_EOF(self, x):
        """EOF signal to exit the program.\n"""

        return True

    def do_emptyline(self, x):
        """ this function returns nothing.\n"""

        print("")

    def do_say_hi(self, usr):
        """this says hi\n"""
        print(f"Hi dear {usr}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
