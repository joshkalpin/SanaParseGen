class Element(object):
    def __init__(self, eleType, eleId, concept, question, answer):
        self.eleType = eleType
        self.eleId = eleId
        self.concept = concept
        self.question = question
        self.answer = answer

    def generatePropertiesDictionary(self):
        return {
            'type': self.eleType,
            'id': self.eleId,
            'concept': self.concept,
            'question': self.question,
            'answer': self.answer
        }

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

        if 'answer' not in attrib:
            raise Exception('Element', 'answer')

    @staticmethod
    def createElement(attrib):
        Element._validateAttributes(attrib)

        if attrib['type'] == 'MULTI_SELECT':
            return MultiSelectElement._createElement(attrib)
        if attrib['type'] == 'ENTRY':
            return EntryElement._createElement(attrib)
        if attrib['type'] == 'PICTURE':
            return PictureElement._createElement(attrib)
        if attrib['type'] == 'GPS':
            return GPSElement._createElement(attrib)

        raise Exception('Element', 'type')


class MultiSelectElement(Element):
    def __init__(self, eleId, concept, question, choices, answer):
        super(MultiSelectElement, self).__init__(
            eleType='MULTI_SELECT',
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer
        )

        self.choices = choices

    def generatePropertiesDictionary(self):
        propDict = super(MultiSelectElement, self).generatePropertiesDictionary()
        propDict['choices'] = self.choices

        return propDict

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
        answer = attrib['answer']

        return MultiSelectElement(
            eleId=eleId,
            concept=concept,
            question=question,
            choices=choices,
            answer=answer
        )


class EntryElement(Element):
    def __init__(self, eleId, concept, question, answer, numeric=None):
        super(EntryElement, self).__init__(
            eleType='ENTRY',
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer
        )
        self.numeric = numeric

    def generatePropertiesDictionary(self):
        propDict = super(EntryElement, self).generatePropertiesDictionary()
        if self.numeric is not None:
            propDict['numeric'] = self.numeric

        return propDict

    @staticmethod
    def _createElement(attrib):
        eleId = attrib['id']
        concept = attrib['concept']
        question = attrib['question']
        answer = attrib['answer']
        numeric = attrib['numeric'] if 'numeric' in attrib else None

        return EntryElement(
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer,
            numeric=numeric
        )


class PictureElement(Element):
    def __init__(self, eleId, concept, question, answer):
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
        answer = attrib['answer']

        return PictureElement(
            eleId=eleId,
            concept=concept,
            question=question,
            answer=answer,
        )


class GPSElement(Element):
    def __init__(self, eleId, concept, question, answer):
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
        answer = attrib['answer']

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

    def generatePropertiesDictionary(self):
        return {
            'title': self.title,
            'author': self.author
        }

    @staticmethod
    def createProcedure(attrib):
        if 'title' not in attrib:
            raise Exception('Procedure', 'title')

        if 'author' not in attrib:
            raise Exception('Procedure', 'author')

        title = attrib['title']
        author = attrib['author']

        return Procedure(title=title, author=author)
