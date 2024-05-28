import unittest
from constants import *
from blocks import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockHeading)

    def test_code(self):
        self.assertEqual(block_to_block_type("```This is a code block```"), BlockCode)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockQuote)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. This is an ordered list"), BlockOrderedList)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- This is an unordered list"), BlockUnorderedList)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockParagraph)

if __name__ == "__main__":
    unittest.main()
