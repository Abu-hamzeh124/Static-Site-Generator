from textnode import TextNode
from generate_page import *
import os
import shutil
import sys

def transfere_files(source_directory: str, destination_directory: str) -> None:
    # التأكد أن المجلدات موجودة
    if not os.path.exists(source_directory) or not os.path.isdir(source_directory):
        print(f"Source directory does not exist: {source_directory}")
        return

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # نسخ كل الملفات والمجلدات من المصدر إلى الوجهة
    for item in os.listdir(source_directory):
        src_path = os.path.join(source_directory, item)
        dest_path = os.path.join(destination_directory, item)
        try:
            if os.path.isdir(src_path):
                # إذا المجلد موجود مسبقًا في الوجهة، نحذفه أولًا
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)
        except Exception as e:
            print(f"Failed to copy {src_path} to {dest_path}. Reason: {e}")

    print(f"Successfully copied all files from {source_directory} to {destination_directory}")


def main():
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
    else:
        basepath = os.getcwd()
    txt_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(txt_node)  # print() يستدعي __repr__ تلقائيًا
    source = r"C:\Users\AbuHamzeh\Static-Site-Generator\static"
    destination = r"C:\Users\AbuHamzeh\Static-Site-Generator\docs"
    transfere_files(
        source,
        destination
    )
    generate_pages_recursive(
        basepath,
        r"C:\Users\AbuHamzeh\Static-Site-Generator\template.html",
        r"C:\Users\AbuHamzeh\Static-Site-Generator\docs"  
    )

main()
   