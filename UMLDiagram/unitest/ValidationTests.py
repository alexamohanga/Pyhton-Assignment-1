import unittest
from UMLDiagram.Parser.PythonParser import PythonParser


class ClassTests(unittest.TestCase):

    # Alex
    def test_valid_file(self):
        python_parser = PythonParser()

        validation_result = python_parser.validate_python_file("../test_data/valid_class.py")

        self.assertTrue(validation_result)

    # Alex
    def test_invalid_file(self):
        python_parser = PythonParser()

        validation_result = python_parser.validate_python_file("../test_data/invalid_class.py")

        self.assertFalse(validation_result)

    # Alex
    def test_wrong_file_path(self):
        python_parser = PythonParser()

        validation_result = python_parser.validate_python_file("../test_data/invalid_class__doesnt_exist.py")

        self.assertFalse(validation_result)


if __name__ == '__main__':
    unittest.main()
