import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        print("to_html_check")
        node = HTMLNode("p", "This is a paragraph")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html_1(self):
        print("props_to_html_check")
        node = HTMLNode("p", "This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(node.props_to_html(), 'class="paragraph"')

    def test_props_to_html_2(self):
        print("props_to_html_check")
        node = HTMLNode("p", "This is a paragraph", props={"class": "paragraph", "id": "123"})
        self.assertEqual(node.props_to_html(), 'class="paragraph" id="123"')


if __name__ == "__main__":
    unittest.main()