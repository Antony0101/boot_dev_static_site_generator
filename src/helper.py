from htmlnode import  LeafNode
from textnode import TextNode

def text_node_to_html_node(text_node):
    if(text_node.text_type  == "text"):
        return LeafNode(None, text_node.text)
    if(text_node.text_type  == "bold"):
        return LeafNode("b", text_node.text)
    if(text_node.text_type  == "italic"):
        return LeafNode("i", text_node.text)
    if(text_node.text_type  == "code"):
        return LeafNode("code", text_node.text)
    if(text_node.text_type  == "link"):
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if(text_node.text_type  == "image"):
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    

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