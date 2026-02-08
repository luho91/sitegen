import re

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    h = re.compile(r'^#{1,6} ')
    if h.match(block):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    blocklines = block.split("\n")
    r = line_to_block_type(blocklines[0])
    ol_count = 1
    for bl in blocklines:
        if line_to_block_type(bl) != r:
            return BlockType.PARAGRAPH

        if r == BlockType.ORDERED_LIST and not bl.startswith(f"{ol_count}. "):
            return BlockType.PARAGRAPH

        ol_count += 1
    return r


def line_to_block_type(line):
    ol = re.compile(r"^\d+\. ")
    if line.startswith(">"):
        return BlockType.QUOTE
    if line.startswith("- "):
        return BlockType.UNORDERED_LIST
    if ol.match(line):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
