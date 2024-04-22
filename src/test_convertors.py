import unittest
from textnode import TextNode
from convertors import text_node_to_html_node
from htmlnode import LeafNode


class TestTextToHtml(unittest.TestCase):
    def test_text_to_html_text(self):
        text_node = TextNode("This is a text node", "text")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, "This is a text node"))

    def test_text_to_html_bold(self):
        text_node = TextNode("This is a text node", "bold")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("b", "This is a text node"))

    def test_text_to_html_italic(self):
        text_node = TextNode("This is a text node", "italic")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("i", "This is a text node"))

    def test_text_to_html_code(self):
        text_node = TextNode("This is a text node", "code")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("code", "This is a text node"))

    def test_text_to_html_link(self):
        text_node = TextNode("This is a text node", "link", "https://example.com")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("a", "This is a text node", {"href": "https://example.com"}))

    def test_text_to_html_image(self):
        text_node = TextNode("This is a text node", "image", "https://example.com")
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("img", None, {"src": "https://example.com", "alt": "This is a text node"}))

if __name__ == "__main__":
    unittest.main()