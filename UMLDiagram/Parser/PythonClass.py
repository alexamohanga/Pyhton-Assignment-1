class PythonClass:
    class_attrib = []

    # Brandon
    def __init__(self, name, indentation):
        self.name = name
        self.indentation = indentation
        self.statements = []
        self.methods = []
        self.attrib = []

    # Brandon
    def add_statement(self, new_statement):
        self.statements.append(new_statement)

    # Brandon
    def extract_from_statements(self):
        self.__extract_attrib()
        self.__extract_methods()

    # Brandon
    def __extract_attrib(self):
        is_class_attributes = True
        self.attrib = []
        for statement in self.statements:
            if statement.is_attrib() or (is_class_attributes and statement.is_assignment()):
                attrib_name = ""
                if statement.is_private():
                    attrib_name += "-"
                elif statement.is_protected():
                    attrib_name += "#"
                elif statement.is_public():
                    attrib_name += "+"

                attrib_name += statement.get_name()
                self.attrib.append(attrib_name)
            else:
                is_class_attributes = False
        pass

    # Brandon
    def __extract_methods(self):
        self.methods = []
        for statement in self.statements:
            if statement.is_def():
                method_name = ""
                if statement.is_private():
                    method_name += "-"
                if statement.is_protected():
                    method_name += "#"
                elif statement.is_public():
                    method_name += "+"

                method_name += statement.get_name().rstrip(")").rstrip(",") + ")"
                self.methods.append(method_name)
