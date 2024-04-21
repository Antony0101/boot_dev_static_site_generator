import unittest

from htmlnode import HTMLNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html_1(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(node.props_to_html(), 'class="paragraph"')

    def test_props_to_html_2(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "paragraph", "id": "123"})
        self.assertEqual(node.props_to_html(), 'class="paragraph" id="123"')


class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("p", "This is a paragraph", {"class": "paragraph"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.props, {"class": "paragraph"})
        self.assertIsNone(node.children)

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", {"class": "paragraph"})
        self.assertEqual(node.to_html(), '<p class="paragraph">This is a paragraph</p>')

    def test_to_html_no_tag(self):
        node = LeafNode(value="This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(node.to_html(), 'This is a paragraph')

    def test_init_no_value(self):
        self.assertRaises(ValueError, LeafNode, "p", None, {"class": "paragraph"})


if __name__ == "__main__":
    unittest.main()