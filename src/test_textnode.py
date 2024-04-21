import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)
    
    def test_neq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)
    
    def test_repr1(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_repr2(self):
        node = TextNode("This is a text node", "bold", "https://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://example.com)")
    
    def test_eq_url(self):
        node1 = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is a text node", "bold", "https://example.com")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()