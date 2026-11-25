from enum import Enum

class TextType(Enum):
    PLAIN = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, input, type, link=None):
        self.text = input
        if type not in TextType:
            raise Exception("Type description error")
        self.text_type = type
        self.url = link

    def __eq__(self, other):
        if (self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url):
            return True
        return False


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    