import re

def extract_markdown_images(text):
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def extract_markdown_links(text):
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def markdown_to_blocks(markdown):
    splited_markdown = markdown.split("\n\n")
    sectioned_list = []
    for section in splited_markdown:
        sectioned_list.append(section.strip())
    return sectioned_list    