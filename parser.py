from models import *


class Parser(object):
    @staticmethod
    def parse_element(elementElement):
        if elementElement.tag != 'Element':
            raise Exception('ElementElement', 'tag')

        element = Element.create_element(elementElement.attrib)

        return element

    @staticmethod
    def parse_page(pageElement):
        if pageElement.tag != 'Page':
            raise Exception('PageElement', 'tag')

        page = Page()

        for pageChild in pageElement:
            if pageChild.tag == 'Element':
                element = Parser.parse_element(pageChild)
                page.elements.append(element)
            else:
                raise Exception('Page', 'child')

        return page

    @staticmethod
    def parse_procedure(procedureElement):
        if procedureElement.tag != 'Procedure':
            raise Exception('ProcedureElement', 'tag')

        procedure = Procedure.create_procedure(procedureElement.attrib)

        for pageElement in procedureElement:
            page = Parser.parse_page(pageElement)
            procedure.pages.append(page)

        return procedure
