from enum import Enum

def markdown_to_blocks(markdown):
    final_list = []
    split_markdown = markdown.split("\n\n")
    for block in split_markdown:
        stripped_block = block.strip()
        if stripped_block:
            final_list.append(stripped_block)
    return final_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if any(line.startswith(("###### ", "##### ", "#### ", "### ", "## ", "# ")) for line in lines):
        return BlockType.HEADING

    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if all(line.startswith(">") for line in lines if line.strip()):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines if line.strip()):
        return BlockType.UNORDERED_LIST

    ordered = True
    for idx, line in enumerate(lines, start=1):
        if line.strip() and not line.startswith(f"{idx}. "):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


        