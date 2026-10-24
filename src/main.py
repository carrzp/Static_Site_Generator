from textnode import TextNode, TextType
import os
import shutil
from markdown_blocks import markdown_to_html_node

def source_to_destination(srcpath, destpath):
    if os.path.exists(destpath):
        shutil.rmtree(destpath)
    os.mkdir(destpath)
    files = os.listdir(srcpath)
    for file in files:
        if os.path.isfile(os.path.join(srcpath, file)):
            shutil.copy(os.path.join(srcpath, file), destpath)
        else:
            source_to_destination(os.path.join(srcpath, file), os.path.join(destpath, file))
            
def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[1:].strip()
        raise Exception("No h1 line detected")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        from_path_read = f.read()

    with open(template_path) as g:
        template_path_read = g.read()

    replace_title_content = template_path_read.replace("{{ Title }}", extract_title(from_path_read)).replace("{{ Content }}", markdown_to_html_node(from_path_read).to_html())
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(replace_title_content)

def main():
    
    source_to_destination("static", "public")    
    generate_page("content/index.md", "template.html", "public/index.html")

main()