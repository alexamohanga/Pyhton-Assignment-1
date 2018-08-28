import doctest
from UMLDiagram.Parser.PythonParser import PythonParser
from UMLDiagram.Parser.PlantUML import PlantUMLProcessor
from UMLDiagram.CLI.cli import CLI

class input_test:
    """
    # Alex
    >>> pythonParser = PythonParser()
    >>> pythonParser.input("invalid.py")
    Validating: invalid.py
    Error: File was not found: invalid.py
    Failed to validate input file: invalid.py

    # Alex
    >>> pythonParser = PythonParser()
    >>> pythonParser.input("../test_data/invalid_class.py")
    Validating: ../test_data/invalid_class.py
    Error: Failed to validate python code. Please provide valid Python code:
    Python Error: invalid syntax (../test_data/invalid_class.py, line 1)
    Failed to validate input file: ../test_data/invalid_class.py

    # Alex
    >>> pythonParser = PythonParser()
    >>> pythonParser.input("../test_data/valid_class.py")
    Validating: ../test_data/valid_class.py
    Successfully Validated: ../test_data/valid_class.py
    Parsed 16 lines
    Removed 7 empty lines

    # Brandon
    >>> pythonParser.parse_classes()
    >>> output = pythonParser.get_plant_uml()
    >>> PlantUMLProcessor.generate(output)
    Successfully generated Plant UML notation and saved it in plantuml.txt
    Class Generation has finished executing, a diagram.png was created

    # Brandon
    >>> cli = CLI()
    <BLANKLINE>
    Welcome to the Python 3 UML CLI Shell!
        Shell by Brandon De Rose
    <BLANKLINE>
    Tip: Type 'help' for a list of commands
    <BLANKLINE>
    <BLANKLINE>
    """


if __name__ == "__main__":
    doctest.testmod()
