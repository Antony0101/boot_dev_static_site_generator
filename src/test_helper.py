import unittest
from textnode import TextNode
from helper import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image,split_nodes_link,text_to_textnodes
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


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![image1](https://example.com/image1.png) ![image2](https://example.com/image2.png)"
        self.assertEqual(extract_markdown_images(text), [("image1", "https://example.com/image1.png"), ("image2", "https://example.com/image2.png")])
    
    def test_extract_markdown_images_2(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")] )


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "[link1](https://example.com/link1) [link2](https://example.com/link2)"
        self.assertEqual(extract_markdown_links(text), [("link1", "https://example.com/link1"), ("link2", "https://example.com/link2")])
    
    def test_extract_markdown_links_2(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])


class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        nodes = [TextNode("This is a ![image1](https://example.com/image1.png) node", "text")]
        resultnodes = [TextNode("This is a ", "text"), TextNode("image1", "image", "https://example.com/image1.png"), TextNode(" node", "text")]
        self.assertEqual(split_nodes_image(nodes), resultnodes)
    
    def test_split_nodes_image_2(self):
        nodes = [TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)","text",)]
        resultnodes = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", "text"),
            TextNode(
                "second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        self.assertEqual(split_nodes_image(nodes), resultnodes)

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        nodes = [TextNode("This is a [link1](https://example.com/link1) node", "text")]
        resultnodes = [TextNode("This is a ", "text"), TextNode("link1", "link", "https://example.com/link1"), TextNode(" node", "text")]
        self.assertEqual(split_nodes_link(nodes), resultnodes)
    
    def test_split_nodes_link_2(self):
        nodes = [TextNode("This is text with a [link](https://www.example.com) and another [second link](https://www.example.com/another)","text",)]
        resultnodes = [
            TextNode("This is text with a ", "text"),
            TextNode("link", "link", "https://www.example.com"),
            TextNode(" and another ", "text"),
            TextNode(
                "second link", "link", "https://www.example.com/another"
            ),
        ]
        self.assertEqual(split_nodes_link(nodes), resultnodes)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is a text node"
        resultnodes = [TextNode("This is a text node", "text")]
        self.assertEqual(text_to_textnodes(text), resultnodes)
    
    def test_text_to_textnodes_2(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        resultnodes = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), resultnodes)