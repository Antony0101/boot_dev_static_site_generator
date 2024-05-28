from constants import *
from htmlnode import LeafNode,ParentNode

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