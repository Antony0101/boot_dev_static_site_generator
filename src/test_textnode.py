import unittest

from textnode import TextNode
from constants import InlineText, InlineBold, InlineItalic, InlineCode, InlineLink, InlineImage


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", InlineBold)
        node2 = TextNode("This is a text node", InlineBold)
        self.assertEqual(node1, node2)
    
    def test_neq(self):
        node1 = TextNode("This is a text node", InlineBold)
        node2 = TextNode("This is a text node", InlineItalic)
        self.assertNotEqual(node1, node2)
    
    def test_repr1(self):
        node = TextNode("This is a text node", InlineBold)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_repr2(self):
        node = TextNode("This is a text node", InlineBold, "https://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://example.com)")
    
    def test_eq_url(self):
        node1 = TextNode("This is a text node", InlineBold, "https://example.com")
        node2 = TextNode("This is a text node", InlineBold, "https://example.com")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()