import unittest
from UMLDiagram.Parser.PythonClass import PythonClass
from UMLDiagram.Parser.PythonStatement import PythonStatement


class ClassTests(unittest.TestCase):

    # Brandon
    def test_default_state(self):
        pyhton_class = PythonClass("TestClass", 0)

        self.assertEqual(pyhton_class.name, "TestClass")
        self.assertEqual(pyhton_class.indentation, 0)
        self.assertEqual(pyhton_class.statements, [])
        self.assertEqual(pyhton_class.methods, [])
        self.assertEqual(pyhton_class.attrib, [])

    # Brandon
    def test_add_statement(self):
        python_class = PythonClass("TestClass", 0)

        self.assertEqual(len(python_class.statements), 0)
        python_class.add_statement(PythonStatement("    def add(self):"))
        self.assertEqual(len(python_class.statements), 1)

        self.assertEqual(len(python_class.methods), 0)
        python_class.extract_from_statements()
        self.assertEqual(len(python_class.methods), 1)

    # Brandon
    def test_add_attrib(self):
        python_class = PythonClass("TestClass", 0)

        self.assertEqual(len(python_class.statements), 0)
        python_class.add_statement(PythonStatement("    self.x = 0"))
        self.assertEqual(len(python_class.statements), 1)

        self.assertEqual(len(python_class.attrib), 0)
        python_class.extract_from_statements()
        self.assertEqual(len(python_class.attrib), 1)


if __name__ == '__main__':
    unittest.main()
