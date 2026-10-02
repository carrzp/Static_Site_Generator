

def markdown_to_blocks(markdown):
    final_list = []
    split_markdown = markdown.split("\n\n")
    for block in split_markdown:
        stripped_block = block.strip()
        if stripped_block:
            final_list.append(stripped_block)
    return final_list

