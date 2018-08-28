class PythonStatement:
    # Brandon
    def __init__(self, line):
        self.items = line.strip().split()
        self.indentation = len(line) - len(line.lstrip())

    # Brandon
    def is_class(self):
        return self.items[0] == "class"

    # Brandon
    def is_def(self):
        return self.items[0] == "def"

    # Brandon
    def is_attrib(self):
        return self.items[0].startswith("self.") and self.get_name() != "None"

    # Brandon
    def is_assignment(self):
        return not self.is_def() and "=" in self.items

    # Brandon
    def is_private(self):
        return self.get_name().startswith("__")

    # Brandon
    def is_protected(self):
        return self.get_name().startswith("_") and not self.get_name().startswith("__")

    # Brandon
    def is_public(self):
        return not self.get_name().startswith("_") and not self.get_name().startswith("__")

    # Brandon
    def get_name(self):
        if len(self.items) > 1:
            if self.is_def() or self.is_class():
                return self.items[1].rstrip(":")
            return self.items[0]
        return "None"
