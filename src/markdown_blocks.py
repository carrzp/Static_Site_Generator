from enum import Enum
from textnode import text_node_to_html_node
from htmlnode import ParentNode, HTMLNode
from text_to_textnode import text_to_text_nodes
from textnode import TextNode, TextType


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

def text_to_children(text) -> list[HTMLNode]:
    child_nodes = []
    new_text_nodes = text_to_text_nodes(text)
    for node in new_text_nodes:
        child_nodes.append(text_node_to_html_node(node))
    return child_nodes
    

def heading_to_HTML(block):
    if not block.startswith("#"):
        raise Exception("Block is not of type HEADING")
    heading_split = block.split(" ", 1)
    heading_count = len(heading_split[0])
    return ParentNode(f"h{heading_count}", text_to_children(heading_split[1]))

def paragraph_to_HTML(block):
    return ParentNode("p", text_to_children(block))

def quote_to_HTML(block):
    if not block.startswith(">"):
        raise Exception("Block is not of type QUOTE")
    quote_split = block.split("\n")
    strip_lines = []
    for line in quote_split:
        strip_lines.append(line.strip("> "))
    final_string = " ".join(strip_lines)
    return ParentNode("blockquote", text_to_children(final_string))

def code_to_HTML(block):
    if not block.startswith("```"):
        raise Exception("Block is not of type CODE")
    else:
        split_code = block.split("```")
        code_text_node = TextNode(split_code[1], TextType.TEXT)
        html_leaf = text_node_to_html_node(code_text_node)
        wrapped = ParentNode("code",[html_leaf])
        outer = ParentNode("pre", [wrapped])
    return outer


def ordered_list_to_HTML(blocktype):
    pass

def unordered_list_to_HTML(blocktype):
    pass

def markdown_to_html_node(markdown) -> HTMLNode:
        blocks = markdown_to_blocks(markdown)
        for block in blocks:
            block_type = block_to_block_type(block)
            new_HTMLNode = HTMLNode()
