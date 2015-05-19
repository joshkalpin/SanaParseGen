class Element(object):
    def __init__(self, eleType, eleId, concept, question, answer):
        self.eleType = eleType
        self.eleId = eleId
        self.concept = concept
        self.question = question
        self.answer = answer

    def generate_properties_dict(self):
        return {
            'type': self.eleType,
            'id': self.eleId,
            'concept': self.concept,
            'question': self.question,
            'answer': self.answer
        }

    @staticmethod
    def _validate_attributes(attrib):
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
    def create_element(attrib):
        Element._validate_attributes(attrib)

        if attrib['type'] == 'MULTI_SELECT':
            return MultiSelectElement._create_element(attrib)
        if attrib['type'] == 'ENTRY':
            return EntryElement._create_element(attrib)
        if attrib['type'] == 'PICTURE':
            return PictureElement._create_element(attrib)
        if attrib['type'] == 'GPS':
            return GPSElement._create_element(attrib)

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

    def generate_properties_dict(self):
        propDict = super(MultiSelectElement, self).generate_properties_dict()
        propDict['choices'] = self.choices

        return propDict

    @staticmethod
    def _validate_attributes(attrib):
        if 'choices' not in attrib:
            raise Exception('MultiSelectElement', 'choices')

    @staticmethod
    def _create_element(attrib):
        MultiSelectElement._validate_attributes(attrib)

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

    def generate_properties_dict(self):
        propDict = super(EntryElement, self).generate_properties_dict()
        if self.numeric is not None:
            propDict['numeric'] = self.numeric

        return propDict

    @staticmethod
    def _create_element(attrib):
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
    def _create_element(attrib):
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
    def _create_element(attrib):
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

    def generate_properties_dict(self):
        return {
            'title': self.title,
            'author': self.author
        }

    @staticmethod
    def create_procedure(attrib):
        if 'title' not in attrib:
            raise Exception('Procedure', 'title')

        if 'author' not in attrib:
            raise Exception('Procedure', 'author')

        title = attrib['title']
        author = attrib['author']

        return Procedure(title=title, author=author)
