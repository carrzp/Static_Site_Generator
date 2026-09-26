from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)

            if len(split_node) % 2 == 0:
                raise Exception(f'Missing an opening or closing "{delimiter}"')

            for i, value in enumerate(split_node):
                if len(value) == 0:
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(value, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(value, text_type))   
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if len(node.text) == 0:
            continue
        
        extract_node = extract_markdown_images(node.text)

        if len(extract_node) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for i, value in enumerate(extract_node):
            sections = remaining_text.split(f"![{value[0]}]({value[1]})", 1)
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(value[0], TextType.IMAGE, value[1]))
            remaining_text = sections[1]

        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
          
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if len(node.text) == 0:
            continue
        
        extract_node = extract_markdown_links(node.text)

        if len(extract_node) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for i, value in enumerate(extract_node):
            sections = remaining_text.split(f"[{value[0]}]({value[1]})", 1)
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(value[0], TextType.LINK, value[1]))
            remaining_text = sections[1]

        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes