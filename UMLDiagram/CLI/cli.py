import sys
from UMLDiagram.Parser.PythonParser import PythonParser
from UMLDiagram.Parser.PlantUML import PlantUMLProcessor


# Brandon
class CLI:
    exit_requested = False
    command_list = []
    help_list = [
        ["help", "This command shows the help text. Like this"],
        ["input", "Opens a Python File and parses it"],
        ["generate", "Generates diagram"],
        ["test", "Runs the program and outputs a class diagram of this package"],
        ["exit", "Exits the application\"s shell."]
    ]

    # Brandon
    def __init__(self):
        # Auto fill the command list from the help list
        for command in self.help_list:
            self.command_list.append(command[0])

        self.python_parser = PythonParser()

        # Welcome messages
        print("\nWelcome to the Python 3 UML CLI Shell!")
        print("    Shell by Brandon De Rose\n")
        print("Tip: Type 'help' for a list of commands\n\n")

    # Brandon
    def check_commandline(self):
        command = ""
        if len(sys.argv) > 1:
            command = sys.argv[1]
        args = []
        if len(sys.argv) > 2:
            args = sys.argv[2:]

        if command not in self.command_list:
            return False
        self.run_command(command, args)
        return True

    # Brandon
    def check_input(self):
        # Get command input from stdin
        command = input("UMLCli# ")
        # Execute the command using method
        argv = command.split(" ")

        self.run_command(argv[0], argv[1:])
        # If exit is not requested then recursively check input again
        if not self.exit_requested:
            self.check_input()

    # Brandon
    def run_command(self, command, args=[]):
        if command == "":
            return
        if command not in self.command_list:
            print("Command not found. Try using the 'help' command.")
            self.check_input()
            return
        getattr(self, command)(args)

    # Alex
    def input(self, args=[]):
        if len(args) == 0:
            print("Please provide a file name with the input command using one argument")
            return
        for arg in args:
            self.python_parser.input(arg)

    # Alex
    def generate(self, args=[]):
        self.python_parser.parse_classes()
        output = self.python_parser.get_plant_uml()
        PlantUMLProcessor.generate(output)

    # Brandon
    def test(self, args=[]):
        self.input([
            "Parser/PythonClass.py",
            "Parser/PythonStatement.py",
            "Parser/PythonParser.py",
            "CLI/cli.py"
        ])
        self.generate()

    # Brandon
    def help(self, args=[]):
        print("\nList of available commands:")
        for help_item in self.help_list:
            print("\t" + help_item[0] + "\t=> " + help_item[1])
        # New line
        print("")

    # Brandon
    def exit(self, args=[]):
        self.exit_requested = True
        print("Bye!\n")

