import re

from enum import Enum
from leafnode import LeafNode
from htmlnode import HTMLNode
from parentnode import ParentNode


class TextType(Enum):
    TEXT = "text (plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url if self.text_type == TextType.IMAGE or self.text_type == TextType.LINK else None


    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Bruh, no compatible node type found ...")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    r = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            r.append(old_node)
        else:
            text_array = old_node.text.split(delimiter)
            text = ""
            if len(text_array) % 2 == 0:
                raise Exception("Uneven amount of delimiters found!")
            
            while len(text_array) > 0:
                # no more delimiters found
                if len(text_array) == 1:
                    r.append(TextNode(text_array[0], TextType.TEXT))
                    break
                text_array, partial_array = text_array[3:], text_array[0:3]
                r.append(TextNode(partial_array[0], TextType.TEXT))
                r.append(TextNode(partial_array[1], text_type))
                r.append(TextNode(partial_array[2], TextType.TEXT))
    return r


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
