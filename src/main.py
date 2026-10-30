from textnode import TextNode, TextType
import os
import shutil
from markdown_blocks import markdown_to_html_node
import pathlib
import sys

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

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        from_path_read = f.read()

    with open(template_path) as g:
        template_path_read = g.read()

    replace_title_content = template_path_read.replace("{{ Title }}", extract_title(from_path_read)).replace("{{ Content }}", markdown_to_html_node(from_path_read).to_html()).replace('href="/', 'href="' + basepath).replace('src="/', 'src="' + basepath)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(replace_title_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_list = os.listdir(dir_path_content)
    for item in content_list:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            generate_page(item_path, template_path, pathlib.Path(dest_path).with_suffix(".html"), basepath)
        else:
            generate_pages_recursive(item_path, template_path, dest_path, basepath)

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    source_to_destination("static", "docs")    
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()