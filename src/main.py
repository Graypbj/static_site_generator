import os
import shutil
from textnode import TextType, TextNode

def remove_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)

def copy_contents(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        try:
            if os.path.isdir(source_item):
                copy_contents(source_item, destination_item)
            else:
                shutil.copy2(source_item, destination_item)
        except Exception as e:
            print(f"Failed to copy {source_item} to {destination_item}. Reason: {e}")

def main():
    public_dir = "./public"
    static_dir = "./static"

    remove_dir(public_dir)
    os.mkdir(public_dir)
    copy_contents(static_dir, public_dir)

main()
