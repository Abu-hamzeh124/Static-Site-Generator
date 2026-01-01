from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    splited_text_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            splited_text_list.append(old_node)
        else:
            splited_old_node = old_node.text.split(delimiter)
            if len(splited_old_node) % 2 == 0:
                raise Exception("Missing closing delimiter")
            new_list = []
            for i in range(len(splited_old_node)):
                part = splited_old_node[i]
                if part == "":
                    continue
                if i % 2 == 0:
                    # outside delimiters
                    new_list.append(TextNode(part, TextType.TEXT))
                else:
                    # inside delimiters
                    new_list.append(TextNode(part, text_type))
            splited_text_list.extend(new_list)        
    return splited_text_list        

def split_nodes_image(old_nodes):
    splited_text_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            splited_text_list.append(old_node)
        else:
            original_text = old_node.text
            new_nodes = []
            extracted = extract_markdown_images(original_text)
            if not extracted:
                splited_text_list.append(old_node)
                continue 
            for image_alt, image_url in extracted: 
                image_markdown = f"![{image_alt}]({image_url})"
                
                parts = original_text.split(image_markdown, 1)
                
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

                if len(parts) > 1:
                    original_text = parts[1]
                else:
                    original_text = "" 
            
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))


            splited_text_list.extend(new_nodes)
    return splited_text_list

def split_nodes_link(old_nodes):
    splited_text_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            splited_text_list.append(old_node)
        else:
            original_text = old_node.text
            new_nodes = []
            extracted = extract_markdown_links(original_text)
            if not extracted:
                splited_text_list.append(old_node)
                continue 
            for image_alt, image_url in extracted: 
                image_markdown = f"[{image_alt}]({image_url})"
                
                parts = original_text.split(image_markdown, 1)
                
                if parts[0] != "":
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                new_nodes.append(TextNode(image_alt, TextType.LINK, image_url))

                if len(parts) > 1:
                    original_text = parts[1]
                else:
                    original_text = "" 
            
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))


            splited_text_list.extend(new_nodes)
    return splited_text_list
# ...existing code...
def text_to_textnodes(text):
    if text is None:
        return []
    text_str = str(text)
    if text_str == "":
        return []
    nodes = [TextNode(text_str, TextType.TEXT)]

    # split images and links first, then code, then bold and italic
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
# ...existing code...