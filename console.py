#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import models
import shlex
import re
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class implemented:
        - quit and EOF to exit the program
        - help by default
        - a custom prompt: (hbnb)
        - an empty line + ENTER shouldn't execute anything
    Attribute:
        - prompt (str)
    """
    prompt = "(hbnb) "
    list_class = ['BaseModel', 'User', 'Place',
                  'State', 'City', 'Amenity', 'Review']

    def do_quit(self, line):
        """quit command to exit the program
        """
        quit()

    def do_EOF(self, line):
        """EOF signal to exit the program
        """
        quit()

    def emptyline(self):
        """Do anything
        """
        pass

    def do_create(self, line):
        """Usage: create <class name> OR <class name>.create()
Def: create command to create a new instance
        """
        my_list = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(line) >= 2:
            var = eval(my_list[0])()
            for i in range(len(line)):
                param = line[i].split('=')
                if len(param) > 1:
                    try:
                        if param[1][0] == "\"":
                            param[1] = param[1].replace('_', ' ')
                            param[1] = param[1].replace("\"", "")
                        elif "." in param[1]:
                            param[1] = float(param[1])
                        else:
                            param[1] = int(param[1])
                    except Exception:
                        continue
                    setattr(var, param[0], param[1])
            models.storage.save()
            print(var.id)
        else:
            var = eval(my_list[0])()
            var.save()
            print(var.id)

    def do_show(self, line):
        """Usage: show <class name> <id> OR <class name>.show(<id>)
Def: show command to print the string representation of an instance
        """
        my_list = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(my_list) < 2:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            key = "{}.{}".format(my_list[0], my_list[1])
            if key in my_dict:
                print(my_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Usage: destroy <class name> OR <class name>.destroy(<id>)
Def: destroy command to delete an instance
        """
        my_list = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(my_list) < 2:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            key = "{}.{}".format(my_list[0], my_list[1])
            if key in my_dict:
                del my_dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Usage: all or all <class> OR <class>.all()
Def: all command to print all string representation of all instance
        """
        my_list = line.split(' ')
        if line == "" or my_list[0] in HBNBCommand.list_class:
            my_list_str = []
            my_str = models.storage.all()
            for key, value in my_str.items():
                if line == "" or type(value) is eval(my_list[0]):
                    my_list_str.append(str(value))
            print("{}".format(my_list_str))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
Usage: <class name>.update(<id>, <attribute name>, <attribute value>)
Def: update command to create or update an instance
        """
        my_list = shlex.split(line)
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(my_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(my_list[0], my_list[1])
            my_dict = models.storage.all().get(key)
            if my_dict is None:
                print("** no instance found **")
            elif len(my_list) < 3:
                print("** attribute name missing **")
            elif len(my_list) < 4:
                print("** value missing **")
            else:
                setattr(my_dict, my_list[2], my_list[3])
                setattr(my_dict, 'updated_at', datetime.now())
                models.storage.save()

    def do_count(self, line):
        """Usage: count <class name> OR <class name>.count()
Def: count command to count the instances of a class
        """
        my_list = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            my_list_dict = []
            my_dict = models.storage.all()
            for value in my_dict:
                if value.startswith(my_list[0] + '.'):
                    my_list_dict.append(value)
            print(len(my_list_dict))

    def default(self, line):
        """Default method when the command is not recognized
        """
        list_method = {
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update,
            "count": self.do_count
        }
        match_1 = re.search(r"\.", line)
        if match_1 is not None:
            my_list_line = [line[:match_1.span()[0]], line[match_1.span()[1]:]]

            match_2 = re.search(r"\((.*?)\)", my_list_line[1])
            if match_2 is not None:
                my_list_cmd = [my_list_line[1][:match_2.span()[0]],
                               match_2.group()[1:-1]]

                if my_list_cmd[0] in list_method.keys():
                    if my_list_cmd[0] == "update":
                        replace = my_list_cmd[1].replace(",", "")
                        result_update = "{} {}".format(my_list_line[0],
                                                       replace)
                        return list_method[my_list_cmd[0]](result_update)

                    elif my_list_cmd[0] != "update":
                        result_all = "{} {}".format(my_list_line[0],
                                                    my_list_cmd[1])
                        return list_method[my_list_cmd[0]](result_all)

        print("*** Unknown syntax: {}".format(line))
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
