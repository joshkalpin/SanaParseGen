from xml.etree import ElementTree
from xml.dom import minidom
from models import *


class Generator:

    @staticmethod
    def _prettify(elem):
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    @staticmethod
    def generateProcedure(procedure):
        procedureElement = ElementTree.Element('Procedure')
        procedureElement.attrib = procedure.generatePropertiesDictionary()

        for page in procedure.pages:
            pageElement = ElementTree.SubElement(procedureElement, 'Page')

            for element in page.elements:
                ElementTree.SubElement(
                    pageElement,
                    'Element',
                    element.generatePropertiesDictionary()
                )

        return Generator._prettify(procedureElement)
