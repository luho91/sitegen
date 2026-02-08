from transformer import markdown_to_blocks
from block import block_to_block_type, BlockType


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    blocks = {x: y for x, y in zip(blocks, list(map(block_to_block_type, blocks)))}
    for b in blocks:
        if blocks[b] == BlockType.HEADING and b.find(" ") == 1:
            return b[2:]

    raise Exception("No Heading found!")
