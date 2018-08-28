import os.path
from UMLDiagram.Parser.PythonClass import PythonClass
from UMLDiagram.Parser.PythonStatement import PythonStatement


class PythonParser:
    # Brandon
    def __init__(self):
        self.class_list = []
        self.statements = []

    # Alex
    def input(self, file_path):
        print("Validating: " + file_path)
        if not self.validate_python_file(file_path):
            print("Failed to validate input file: " + file_path)
            return

        print("Successfully Validated: " + file_path)
        self.parse(file_path)

    # Alex
    @staticmethod
    def validate_python_file(file_path):
        if not os.path.isfile(file_path):
            print("Error: File was not found: " + file_path)
            return False

        # Alex exception handling
        try:
            source = open(file_path, 'r').read() + '\n'
            compile(source, file_path, 'exec')
        except SyntaxError as e:
            print("Error: Failed to validate python code. Please provide valid Python code:\nPython Error: " + str(e))
            return False
        except SyntaxWarning as e:
            print("Warning: A syntax warning was found:\nPython Warning: " + str(e))
            print("This application will try to continue")

        return True

    # Brandon
    def parse(self, file_path):
        # Alex
        source = open(file_path, 'r').read() + '\n'

        # Brandon
        file_lines = source.split("\n")
        original_count = len(file_lines)

        for i, line in enumerate(file_lines):
            sline = line.strip()
            if sline == "" or sline.startswith("#"):
                # Removes single item from list at index 'i'
                file_lines = file_lines[:i] + file_lines[i+1:]
                continue
            self.statements.append(PythonStatement(line))

        print("Parsed " + str(original_count) + " lines")
        print("Removed " + str(original_count - len(file_lines)) + " empty lines")

    # Brandon
    def parse_classes(self):
        current_class = None
        for statement in self.statements:
            if statement.is_class():
                current_class = PythonClass(statement.get_name(), statement.indentation)
                self.class_list.append(current_class)
            else:
                if current_class is not None:
                    if current_class.indentation > statement.indentation:
                        current_class = None
                    else:
                        current_class.add_statement(statement)

        for a_class in self.class_list:
            a_class.extract_from_statements()

    # Brandon
    def get_plant_uml(self):
        output_uml = "@startuml\n"

        for a_class in self.class_list:
            output_uml += "class " + a_class.name + " {\n"

            # Print Each attribute
            for a_attrib in a_class.attrib:
                output_uml += "\t" + a_attrib + "\n"
            # Spacer
            if len(a_class.attrib) > 0 and len(a_class.methods) > 0:
                output_uml += "\n"
            # Print Each Method
            for a_method in a_class.methods:
                output_uml += "\t" + a_method + "\n"

            output_uml += "}\n"

        output_uml += "@enduml\n"
        return output_uml
