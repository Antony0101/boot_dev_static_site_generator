import unittest
from textnode import TextNode
from helper import text_node_to_html_node, split_nodes_delimiter
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


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [TextNode("This is a *text* node", "text")]
        resultnodes = [TextNode("This is a ", "text"), TextNode("text", "bold"), TextNode(" node", "text")]
        self.assertEqual(split_nodes_delimiter(nodes, "*", "bold"), resultnodes)
    
    def test_split_nodes_delimiter_no_closing_delimiter(self):
        nodes = [TextNode("This is a *text node", "text")]
        self.assertRaises(ValueError, split_nodes_delimiter, nodes, "*", "bold")

    def test_split_nodes_delimiter_multiple_delimiters(self):
        nodes = [TextNode("This is a *text* node with *multiple* delimiters", "text")]
        resultnodes = [TextNode("This is a ", "text"), TextNode("text", "bold"), TextNode(" node with ", "text"), TextNode("multiple", "bold"), TextNode(" delimiters", "text")]
        self.assertEqual(split_nodes_delimiter(nodes, "*", "bold"), resultnodes)