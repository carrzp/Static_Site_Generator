from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    new_node = [TextNode(text, TextType.TEXT)]
    delim_bold = split_nodes_delimiter(new_node, "**", TextType.BOLD)
    delim_ital = split_nodes_delimiter(delim_bold, "_", TextType.ITALIC)
    delim_code = split_nodes_delimiter(delim_ital, "`", TextType.CODE)
    split_image_node = split_nodes_image(delim_code)
    split_link_node = split_nodes_link(split_image_node)
    return split_link_node