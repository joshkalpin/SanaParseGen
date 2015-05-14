from xml.etree import ElementTree
import sys


class Element(object):
    def __init__(self, eleType, eleId, concept, question, answer=None):
        self.eleType = eleType
        self.eleId = eleId
        self.concept = concept
        self.question = question
        self.answer = answer

    @staticmethod
    def _validateAttributes(attrib):
        if 'type' not in attrib:
            raise Exception('Element', 'type')

        if 'id' not in attrib:
            raise Exception('Element', 'id')

        if 'concept' not in attrib:
            raise Exception('Element', 'concept')

        if 'question' not in attrib:
            raise Exception('Element', 'question')

    @staticmethod
    def createElement(attrib):
        Element._validateAttributes(attrib)

        if attrib['type'] == 'MULTI_SELECT':
            MultiSelectElement._createElement(attrib)
        elif attrib['type'] == 'ENTRY':
            EntryElement._createElement(attrib)
        elif attrib['type'] == 'PICTURE':
            PictureElement._createElement(attrib)
        elif attrib['type'] == 'GPS':
            GPSElement._createElement(attrib)
        else:
            raise Exception('Element', 'type')


class MultiSelectElement(Element):
    def __init__(self, eleId, concept, question, choices, answer=None):
        super(MultiSelectElement, self).__init__(
            eleType='MULTI_SELECT',
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer
        )

        self.choices = choices

    @staticmethod
    def _validateAttributes(attrib):
        if 'choices' not in attrib:
            raise Exception('MultiSelectElement', 'choices')

    @staticmethod
    def _createElement(attrib):
        MultiSelectElement._validateAttributes(attrib)

        eleId = attrib['id']
        concept = attrib['concept']
        question = attrib['question']
        choices = attrib['choices']
        answer = attrib['answer'] if 'answer' in attrib else None

        return MultiSelectElement(
            eleId=eleId,
            concept=concept,
            question=question,
            choices=choices,
            answer=answer
        )


class EntryElement(Element):
    def __init__(self, eleId, concept, question, answer=None, numeric=None):
        super(EntryElement, self).__init__(
            eleType='ENTRY',
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer
        )
        self.numeric = numeric

    @staticmethod
    def _createElement(attrib):
        eleId = attrib['id']
        concept = attrib['concept']
        question = attrib['question']
        answer = attrib['answer'] if 'answer' in attrib else None
        numeric = attrib['numeric'] if 'numeric' in attrib else None

        return EntryElement(
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer,
            numeric=numeric
        )


class PictureElement(Element):
    def __init__(self, eleId, concept, question, answer=''):
        super(PictureElement, self).__init__(
            eleType='PICTURE',
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer
        )

    @staticmethod
    def _createElement(attrib):
        eleId = attrib['id']
        concept = attrib['concept']
        question = attrib['question']
        answer = attrib['answer'] if 'answer' in attrib else None

        return PictureElement(
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer,
        )


class GPSElement(Element):
    def __init__(self, eleId, concept, question, answer=''):
        super(GPSElement, self).__init__(
            eleType='GPS',
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer
        )

    @staticmethod
    def _createElement(attrib):
        eleId = attrib['id']
        concept = attrib['concept']
        question = attrib['question']
        answer = attrib['answer'] if 'answer' in attrib else None

        return PictureElement(
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer,
        )


class Page(object):

    def __init__(self):
        self.elements = []


class Procedure(object):

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = []

    def __contains__(self, page):
        return page in self.pages

    @staticmethod
    def createProcedure(attrib):
        if 'title' not in attrib:
            raise Exception('Procedure', 'title')

        if 'author' not in attrib:
            raise Exception('Procedure', 'author')

        title = attrib['title']
        author = attrib['author']

        return Procedure(title=title, author=author)


def parseElement(elementElement):
    if elementElement.tag != 'Element':
        raise Exception('ElementElement', 'tag')

    element = Element.createElement(elementElement.attrib)

    return element


def parsePage(pageElement):
    if pageElement.tag != 'Page':
        raise Exception('PageElement', 'tag')

    page = Page()

    for pageChild in pageElement:
        if pageChild.tag == 'Element':
            element = parseElement(pageChild)
            page.elements.append(element)
        else:
            raise Exception('Page', 'child')

    return page


def parseProcedure(procedureElement):
    if procedureElement.tag != 'Procedure':
        raise Exception('ProcedureElement', 'tag')

    procedure = Procedure.createProcedure(procedureElement.attrib)
    print procedure.title, procedure.author

    for pageElement in procedureElement:
        page = parsePage(pageElement)
        procedure.pages.append(page)

    return procedure


def main():
    args = sys.argv

    if len(args) != 2:
        print 'ERROR: Pass in the xml file name'
        exit(1)

    try:
        tree = ElementTree.parse(args[1])
        procedureElement = tree.getroot()
        procedure = parseProcedure(procedureElement)

        print len(procedure.pages)
    except IOError:
        print 'ERROR: Invalid filename'
        exit(1)

if __name__ == '__main__':
    main()