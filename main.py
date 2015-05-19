from xml.etree import ElementTree
from parser import *
from generator import *
import sys


def main():
    args = sys.argv

    if len(args) != 2:
        print 'ERROR: Pass in the xml file name'
        exit(1)

    try:
        tree = ElementTree.parse(args[1])
        procedureElement = tree.getroot()
        procedure = Parser.parse_procedure(procedureElement)

        generatedProc = Generator.generate_procedure(procedure)
        with open('out.xml', 'w') as outfile:
            outfile.write(generatedProc)

        print generatedProc

    except IOError:
        print 'ERROR: Invalid filename'
        exit(1)

if __name__ == '__main__':
    main()
