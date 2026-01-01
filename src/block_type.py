from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    cleaned = block.strip()
    if cleaned.startswith("#"):
        return BlockType.HEADING
    if cleaned.startswith("```") and cleaned.endswith("```"):
        return BlockType.CODE
    splited_block = cleaned.split("\n")
    num_of_quotes = 0
    num_of_unordered = 0
    num_of_ordered = 0
    x = 0
    for section in splited_block:
        cleaned_section = section.strip()
        x += 1
        if cleaned_section.startswith(">"):
            num_of_quotes += 1
        elif cleaned_section.startswith("- "):
            num_of_unordered += 1
        elif cleaned_section.startswith(f"{x}. "):  
            num_of_ordered += 1
    if num_of_quotes == len(splited_block):
        return BlockType.QUOTE
    if num_of_unordered == len(splited_block):
        return BlockType.UNORDERED
    if num_of_ordered == len(splited_block):
        return BlockType.ORDERED
    return BlockType.PARAGRAPH              