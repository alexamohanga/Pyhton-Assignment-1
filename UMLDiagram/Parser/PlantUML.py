from plantuml import PlantUML
import os


# Brandon
class PlantUMLProcessor:
    uml_dump_file = "plantuml.txt"
    diagram_image_file = "diagram.png"
    error_file = "errors.txt"

    # Brandon, but based on JigNesh's UML class
    @staticmethod
    def generate(input_uml):
        plant_uml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        PlantUMLProcessor.dump_to_file(input_uml, PlantUMLProcessor.uml_dump_file)
        print("Successfully generated Plant UML notation and saved it in " + PlantUMLProcessor.uml_dump_file)

        PlantUMLProcessor.remove_file(PlantUMLProcessor.diagram_image_file)
        PlantUMLProcessor.remove_file(PlantUMLProcessor.error_file)

        plant_uml.processes_file(PlantUMLProcessor.uml_dump_file, PlantUMLProcessor.diagram_image_file,
                                 PlantUMLProcessor.error_file)

        if not os.path.isfile(PlantUMLProcessor.error_file):
            print("Class Generation has finished executing, a diagram.png was created")
        else:
            print("An error occurred, please check " + PlantUMLProcessor.error_file +
                  " for any errors regarding the Plant UML diagram generation")

    # Brandon
    @staticmethod
    def remove_file(file_name):
        if os.path.isfile(file_name):
            os.remove(file_name)

    # Brandon
    @staticmethod
    def dump_to_file(input_uml, file_name):
        PlantUMLProcessor.remove_file(file_name)

        file = open(file_name, 'w')
        file.write(input_uml)
        file.close()
