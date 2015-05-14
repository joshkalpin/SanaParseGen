from models import *


class Parser(object):
    @staticmethod
    def parseElement(elementElement):
        if elementElement.tag != 'Element':
            raise Exception('ElementElement', 'tag')

        element = Element.createElement(elementElement.attrib)

        return element

    @staticmethod
    def parsePage(pageElement):
        if pageElement.tag != 'Page':
            raise Exception('PageElement', 'tag')

        page = Page()

        for pageChild in pageElement:
            if pageChild.tag == 'Element':
                element = Parser.parseElement(pageChild)
                page.elements.append(element)
            else:
                raise Exception('Page', 'child')

        return page

    @staticmethod
    def parseProcedure(procedureElement):
        if procedureElement.tag != 'Procedure':
            raise Exception('ProcedureElement', 'tag')

        procedure = Procedure.createProcedure(procedureElement.attrib)

        for pageElement in procedureElement:
            page = Parser.parsePage(pageElement)
            procedure.pages.append(page)

        return procedure
