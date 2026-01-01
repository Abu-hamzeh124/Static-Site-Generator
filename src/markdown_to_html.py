from extract_markdown import *
from block_type import *
from htmlnode import ParentNode, LeafNode
from textnode import *
from split_nodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def block_type_to_tags(type1):
    tag = None
    if type1 == BlockType.HEADING:
        tag = 'h1'
    elif type1 == BlockType.PARAGRAPH:
        tag = 'p'
    elif  type1 == BlockType.CODE:
        tag = 'code'
    elif type1 == BlockType.UNORDERED:
        tag = 'ul'
    elif type1 == BlockType.ORDERED:
        tag = 'ol'
    elif type1 == BlockType.QUOTE:
        tag = 'blockquote'
    return tag

def text_to_children(text):
    if text is None:
        return []
    text_nodes = text_to_textnodes(text)
    children = []
    for tn in text_nodes:
        children.append(text_node_to_html_node(tn))
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        type_block = block_to_block_type(block)
        if type_block == BlockType.HEADING:
            # remove leading # characters
            content = block.lstrip('#').strip()
            block_nodes.append(ParentNode('h1', text_to_children(content)))
        elif type_block == BlockType.PARAGRAPH:
            block_nodes.append(ParentNode('p', text_to_children(block)))
        elif type_block == BlockType.CODE:
            inner = block
            if inner.startswith('```') and inner.endswith('```'):
                inner = inner[3:-3]
            block_nodes.append(LeafNode('code', inner))
        elif type_block == BlockType.UNORDERED or type_block == BlockType.ORDERED:
            lines = [ln.strip() for ln in block.split('\n') if ln.strip() != ""]
            items = []
            for i, line in enumerate(lines, start=1):
                if line.startswith('- '):
                    content = line[2:]
                else:
                    # ordered like '1. item'
                    parts = line.split('. ', 1)
                    content = parts[1] if len(parts) > 1 else line
                items.append(ParentNode('li', text_to_children(content)))
            tag = 'ul' if type_block == BlockType.UNORDERED else 'ol'
            block_nodes.append(ParentNode(tag, items))
        elif type_block == BlockType.QUOTE:
            # combine lines into a single paragraph inside blockquote
            lines = [ln.lstrip('> ').strip() for ln in block.split('\n')]
            combined = '\n'.join([ln for ln in lines if ln != ""])
            block_nodes.append(ParentNode('blockquote', [ParentNode('p', text_to_children(combined))]))
        else:
            block_nodes.append(ParentNode('p', text_to_children(block)))

    return ParentNode('div', block_nodes)

