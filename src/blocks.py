from constants import *
from htmlnode import LeafNode,ParentNode
from convertors import markdown_to_blocks, text_node_to_html_node
from inline_spliters import text_to_textnodes

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockHeading
    if block.startswith("```") and block.endswith("```"):
        return BlockCode
    if block.startswith(">"):
        return BlockQuote
    if block.startswith("1. "):
        return BlockOrderedList
    if block.startswith("- ") or block.startswith("* "):
        return BlockUnorderedList
    return BlockParagraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockParagraph:
        return paragraph_block_to_html_node(block)
    if block_type == BlockHeading:
        return heading_block_to_htmlNode(block)
    if block_type == BlockCode:
        return code_block_to_html(block)
    if block_type == BlockOrderedList:
        return olist_block_to_html_node(block)
    if block_type == BlockUnorderedList:
        return ulist_block_to_html_node(block)
    if block_type == BlockQuote:
        return quote_block_to_html(block)
    raise ValueError("Invalid block type")


def heading_block_to_htmlNode(heading_block):
    level = 0
    while heading_block[level] == "#":
        level += 1
    # return f"<h{level}>{heading_block[level+1:]}</h{level}>"
    return LeafNode(f"h{level}", heading_block[level+1:])

def code_block_to_html(code_block):
    # return f"<pre><code>{code_block[3:-3]}</code></pre>"
    return LeafNode("pre", LeafNode("code", code_block[3:-3]))

def quote_block_to_html(quote_block):
    # return f"<blockquote>{quote_block[2:]}</blockquote>"
    return LeafNode("blockquote", quote_block[2:])

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    # print(text,":::",text_nodes,";;;;")
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_block_to_html_node(paragraph_block):
    # return f"<p>{paragraph_block}</p>"
    lines = paragraph_block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    print(children)
    return ParentNode("p", children, None)
    # if len(children) == 1:
    #     return LeafNode("p", children)
    # else :
    #     return ParentNode("p", children)

def olist_block_to_html_node(olist_block):
    items = olist_block.split("\n")
    children = []
    for item in items:
        if item.startswith("1. "):
            item = item[3:]
        else:
            item = item[2:]
        children.append(LeafNode("li", item))
    return ParentNode("ol", children, None)

def ulist_block_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)