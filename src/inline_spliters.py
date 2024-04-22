from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes:list[TextNode], delimiter, text_type):
    new_nodes = []
    for i in range(len(old_nodes)):
        node = old_nodes[i]
        if(node.text_type != "text"):
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if(len(parts)%2 == 0):
            raise ValueError("Closing Delimiter not found")
        for j in range(len(parts)):
            if(j%2 == 0):
                new_nodes.append(TextNode(parts[j], "text"))
            else:
                new_nodes.append(TextNode(parts[j], text_type))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for i in range(len(old_nodes)):
        node = old_nodes[i]
        if(node.text_type != "text"):
            new_nodes.append(node)
            continue
        parts = extract_markdown_images(node.text)
        if(len(parts) == 0):
            new_nodes.append(node)
            continue
        text = node.text
        for j in range(len(parts)):
            text_splits = text.split(f"![{parts[j][0]}]({parts[j][1]})",1)
            text = text_splits[1]
            if(text_splits[0] != ""):
                new_nodes.append(TextNode(text_splits[0], "text"))
            new_nodes.append(TextNode(parts[j][0], "image", parts[j][1]))
        if(text != ""):
            new_nodes.append(TextNode(text, "text"))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for i in range(len(old_nodes)):
        node = old_nodes[i]
        if(node.text_type != "text"):
            new_nodes.append(node)
            continue
        parts = extract_markdown_links(node.text)
        if(len(parts) == 0):
            new_nodes.append(node)
            continue
        text = node.text
        for j in range(len(parts)):
            text_splits = text.split(f"[{parts[j][0]}]({parts[j][1]})",1)
            text = text_splits[1]
            if(text_splits[0] != ""):
                new_nodes.append(TextNode(text_splits[0], "text"))
            new_nodes.append(TextNode(parts[j][0], "link", parts[j][1]))
        if(text != ""):
            new_nodes.append(TextNode(text, "text"))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    return nodes