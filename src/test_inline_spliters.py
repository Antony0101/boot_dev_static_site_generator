import unittest
from textnode import TextNode
from inline_spliters import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image,split_nodes_link,text_to_textnodes
from htmlnode import LeafNode
from constants import InlineText, InlineBold, InlineItalic, InlineCode, InlineLink, InlineImage


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [TextNode("This is a *text* node", InlineText)]
        resultnodes = [TextNode("This is a ", InlineText), TextNode(InlineText, InlineBold), TextNode(" node", InlineText)]
        self.assertEqual(split_nodes_delimiter(nodes, "*", InlineBold), resultnodes)
    
    def test_split_nodes_delimiter_no_closing_delimiter(self):
        nodes = [TextNode("This is a *text node", InlineText)]
        self.assertRaises(ValueError, split_nodes_delimiter, nodes, "*", InlineBold)


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![image1](https://example.com/image1.png) ![image2](https://example.com/image2.png)"
        self.assertEqual(extract_markdown_images(text), [("image1", "https://example.com/image1.png"), ("image2", "https://example.com/image2.png")])
    
    def test_extract_markdown_images_2(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [(InlineImage, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")] )


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "[link1](https://example.com/link1) [link2](https://example.com/link2)"
        self.assertEqual(extract_markdown_links(text), [("link1", "https://example.com/link1"), ("link2", "https://example.com/link2")])
    
    def test_extract_markdown_links_2(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text), [(InlineLink, "https://www.example.com"), ("another", "https://www.example.com/another")])


class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        nodes = [TextNode("This is a ![image1](https://example.com/image1.png) node", InlineText)]
        resultnodes = [TextNode("This is a ", InlineText), TextNode("image1", InlineImage, "https://example.com/image1.png"), TextNode(" node", InlineText)]
        self.assertEqual(split_nodes_image(nodes), resultnodes)
    
    def test_split_nodes_image_2(self):
        nodes = [TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",InlineText,)]
        resultnodes = [
            TextNode("This is text with an ", InlineText),
            TextNode(InlineImage, InlineImage, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", InlineText),
            TextNode(
                "second image", InlineImage, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        self.assertEqual(split_nodes_image(nodes), resultnodes)

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        nodes = [TextNode("This is a [link1](https://example.com/link1) node", InlineText)]
        resultnodes = [TextNode("This is a ", InlineText), TextNode("link1", InlineLink, "https://example.com/link1"), TextNode(" node", InlineText)]
        self.assertEqual(split_nodes_link(nodes), resultnodes)
    
    def test_split_nodes_link_2(self):
        nodes = [TextNode("This is text with a [link](https://www.example.com) and another [second link](https://www.example.com/another)",InlineText,)]
        resultnodes = [
            TextNode("This is text with a ", InlineText),
            TextNode(InlineLink, InlineLink, "https://www.example.com"),
            TextNode(" and another ", InlineText),
            TextNode(
                "second link", InlineLink, "https://www.example.com/another"
            ),
        ]
        self.assertEqual(split_nodes_link(nodes), resultnodes)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is a text node"
        resultnodes = [TextNode("This is a text node", InlineText)]
        self.assertEqual(text_to_textnodes(text), resultnodes)
    
    def test_text_to_textnodes_2(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        resultnodes = [
            TextNode("This is ", InlineText),
            TextNode(InlineText, InlineBold),
            TextNode(" with an ", InlineText),
            TextNode(InlineItalic, InlineItalic),
            TextNode(" word and a ", InlineText),
            TextNode("code block", InlineCode),
            TextNode(" and an ", InlineText),
            TextNode(InlineImage, InlineImage, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", InlineText),
            TextNode(InlineLink, InlineLink, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), resultnodes)

if __name__ == "__main__":
    unittest.main()