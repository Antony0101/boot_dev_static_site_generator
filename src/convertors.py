from htmlnode import  LeafNode
from constants import InlineText, InlineBold, InlineItalic, InlineCode, InlineLink, InlineImage



def text_node_to_html_node(text_node):
    if(text_node.text_type  == InlineText):
        return LeafNode(None, text_node.text)
    if(text_node.text_type  == InlineBold):
        return LeafNode("b", text_node.text)
    if(text_node.text_type  == InlineItalic):
        return LeafNode("i", text_node.text)
    if(text_node.text_type  == InlineCode):
        return LeafNode(InlineCode, text_node.text)
    if(text_node.text_type  == InlineLink):
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if(text_node.text_type  == InlineImage):
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    
def markdown_to_blocks(markdown):
    return [block.strip(" \n").lstrip(" \n") for block in markdown.split("\n\n") if block.strip(" \n").lstrip(" \n") != ""]