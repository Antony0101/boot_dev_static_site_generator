import unittest
from textnode import TextNode
from convertors import text_node_to_html_node, markdown_to_blocks
from htmlnode import LeafNode
from constants import *



class TestTextToHtml(unittest.TestCase):
    def test_text_to_html_text(self):
        text_node = TextNode("This is a text node", InlineText)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, "This is a text node"))

    def test_text_to_html_bold(self):
        text_node = TextNode("This is a text node", InlineBold)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("b", "This is a text node"))

    def test_text_to_html_italic(self):
        text_node = TextNode("This is a text node", InlineItalic)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("i", "This is a text node"))

    def test_text_to_html_code(self):
        text_node = TextNode("This is a text node", InlineCode)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(InlineCode, "This is a text node"))

    def test_text_to_html_link(self):
        text_node = TextNode("This is a text node", InlineLink, "https://example.com")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("a", "This is a text node", {"href": "https://example.com"}))

    def test_text_to_html_image(self):
        text_node = TextNode("This is a text node", InlineImage, "https://example.com")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("img", None, {"src": "https://example.com", "alt": "This is a text node"}))


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown =  '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
'''
        self.assertEqual(markdown_to_blocks(markdown), ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is a list item\n* This is another list item"])

if __name__ == "__main__":
    unittest.main()