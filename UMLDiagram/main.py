from UMLDiagram.CLI.cli import CLI

if __name__ == "__main__":
    theCli = CLI()
    if not theCli.check_commandline():
        theCli.check_input()
