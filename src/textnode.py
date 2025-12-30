from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, txt_node):
        if txt_node.text == self.text and txt_node.text_type == self.text_type and txt_node.url == self.url:
            return True
        return (
            self.text == txt_node.text and
            self.text_type == txt_node.text_type and
            self.url == txt_node.url
        )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"  
    