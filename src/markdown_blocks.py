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

def block_to_block_type(block: str) -> BlockType:
    block = block.strip()
    lines = block.split("\n")
    print(repr(block))

    if lines[0].strip().startswith("```") and lines[-1].strip().startswith("```"):
            return BlockType.CODE
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
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
    final_str = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(final_str))

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
        split_code = block.split("\n")
        content_lines = split_code[1:-1]
        join = "\n".join(content_lines) + "\n"
        code_text_node = TextNode(join, TextType.TEXT)
        html_leaf = text_node_to_html_node(code_text_node)
        wrapped = ParentNode("code",[html_leaf])
        outer = ParentNode("pre", [wrapped])
    return outer


def ordered_list_to_HTML(block):
    ol_nodes = []
    if not block.startswith("1. "):
        raise Exception("Block is not of type ORDERED_LIST")
    split_block = block.split("\n")
    for line in split_block:
        number, item_text = line.split(". ", 1)
        nodes = text_to_children(item_text)
        inner = ParentNode("li", nodes)
        ol_nodes.append(inner) 
    outer = ParentNode("ol", ol_nodes)
    return outer

def unordered_list_to_HTML(block):
    li_nodes = []
    if not block.startswith("- "):
        raise Exception("Block is not of type UNORDERED_LIST")
    split_block = block.split("\n")
    for line in split_block:
        nodes = text_to_children(line[2:])
        inner = ParentNode("li", nodes)
        li_nodes.append(inner) 
    outer = ParentNode("ul", li_nodes)
    return outer
            
def markdown_to_html_node(markdown) -> HTMLNode:
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block_nodes.append(paragraph_to_HTML(block))
        elif block_type == BlockType.HEADING:
            block_nodes.append(heading_to_HTML(block))
        elif block_type == BlockType.QUOTE:
            block_nodes.append(quote_to_HTML(block))
        elif block_type == BlockType.UNORDERED_LIST:
            block_nodes.append(unordered_list_to_HTML(block))
        elif block_type == BlockType.ORDERED_LIST:
            block_nodes.append(ordered_list_to_HTML(block))
        elif block_type == BlockType.CODE:
            block_nodes.append(code_to_HTML(block))
    return ParentNode("div", block_nodes)
