from textnode import TextNode
from constants import InlineText, InlineBold, InlineItalic, InlineCode, InlineLink, InlineImage


def main():
    text_node = TextNode("Hello, World!", InlineText, "https://example.com")
    print(text_node)

if __name__ == "__main__":
    main()