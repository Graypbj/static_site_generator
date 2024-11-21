import os
from markdown_blocks import (
    markdown_to_html_node,
)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[0:2] == "# ":
            header = line[2:]
            return header.strip()
    raise Exception("No header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r", encoding="utf-8") as markdown_file:
        markdown_contents = markdown_file.read()

    with open(template_path, "r", encoding="utf-8") as template_file:
        template_contents = template_file.read()
    
    html_node = markdown_to_html_node(markdown_contents)
    html_contents = html_node.to_html()

    page_title = extract_title(markdown_contents)

    final_html = template_contents.replace("{{ Title }}", page_title).replace("{{ Content }}", html_contents)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(final_html)
    
    print(f"Page successfully generated as {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                relative_path = os.path.relpath(root, dir_path_content)
                source_path = os.path.join(root, file)
                dest_subdir = os.path.join(dest_dir_path, relative_path)
                dest_path = os.path.join(dest_subdir, file.replace(".md", ".html"))

                generate_page(source_path, template_path, dest_path)
