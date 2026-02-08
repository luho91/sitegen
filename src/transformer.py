from textnode import TextNode, TextType, text_to_textnodes, text_node_to_html_node
from block import BlockType, block_to_block_type
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode


def markdown_to_blocks(markdown):
    arr = markdown.split("\n\n")
    r = []
    for l in arr:
        l = l.strip()
        if l == "":
            continue
        else:
            r.append(l)

    return r


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    r = []
    for b in blocks:
        b_type = block_to_block_type(b)
        children_string = strip_dad_stink(b, b_type)

        match b_type:
            case BlockType.PARAGRAPH:
                dad = ParentNode("p", children=list(map(text_node_to_html_node, text_to_textnodes(children_string))))
            case BlockType.HEADING:
                heading_level = b.find(" ")
                dad = ParentNode(f"h{heading_level}", children=list(map(text_node_to_html_node, text_to_textnodes(children_string))))
            case BlockType.CODE:
                dad = ParentNode("pre", children=[text_node_to_html_node(TextNode(children_string, TextType.CODE))])
            case BlockType.QUOTE:
                dad = ParentNode("blockquote", children=list(map(text_node_to_html_node, text_to_textnodes(children_string))))
            case BlockType.UNORDERED_LIST:
                html_children = list(map(add_child_stink, children_string.split("\n")))
                dad = ParentNode("ul", children=[ParentNode("li", children=x) for x in html_children])
            case BlockType.ORDERED_LIST:
                html_children = list(map(add_child_stink, children_string.split("\n")))
                dad = ParentNode("ol", children=[ParentNode("li", children=x) for x in html_children])
            case _:
                raise TypeError("Woah there, what kind of block is this?")

        r.append(dad)
    return ParentNode("div", children=r)


def strip_dad_stink(block, blocktype):
    match blocktype:
        case BlockType.PARAGRAPH:
            return "<br />".join(block.split("\n"))
        case BlockType.HEADING:
            heading_level = block.find(" ")
            if heading_level == -1 or heading_level > 6:
                raise Exception("Somehow we have created a corrupt heading ...")
            return block[heading_level + 1:]
        case BlockType.CODE:
            return block[4:-3]
        case BlockType.QUOTE:
            lines = block.split("\n")
            r = []
            for l in lines:
                r.append(l[2:])
            return "\n".join(r)
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            r = []
            for l in lines:
                r.append(l[2:])
            return "\n".join(r)
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            r = []
            for i in range(len(lines)):
                r.append(lines[i][i // 10 + 3:])
            return "\n".join(r)
        case _:
            raise Exception("Unknown Block Type!")


def add_child_stink(children_string):
    return list(map(text_node_to_html_node, text_to_textnodes(children_string)))
