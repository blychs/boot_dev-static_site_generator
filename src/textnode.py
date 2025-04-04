from enum import Enum
from htmlnode import LeafNode


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

    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        return self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    value = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=value)
        case TextType.BOLD:
            return LeafNode(tag="b", value=value)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=value)
        case TextType.CODE:
            return LeafNode(tag="code", value=value)
        case TextType.LINK:
            return LeafNode(tag="a", value=value,
                            props={"href", text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="",
                            props={"src": text_node.url, "alt": value})
        case _:
            raise TypeError("text_type not valid")
