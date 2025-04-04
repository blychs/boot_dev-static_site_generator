import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def block_to_block_type(markdown_block):
    if re.search(r'^[#]{1,6} ', markdown_block.strip()):
        return BlockType.HEADING
    if markdown_block.strip().startswith(r"```") and markdown_block.strip().endswith(r"```"):
        return BlockType.CODE
    lines = markdown_block.strip().split('\n')
    lines = [line.strip() for line in lines]
    if all(start.startswith('>') for start in lines):
        return BlockType.QUOTE
    if all(start.startswith('-') for start in lines):
        return BlockType.UNORDERED_LIST
    if all(start.startswith(f"{i+1}.") for (i, start) in enumerate(lines)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
