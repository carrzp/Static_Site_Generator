from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
import unittest

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
            ],
        )

    def test_extra_blank_lines_are_ignored(self):
        md = """

First block


Second block


"""
        self.assertEqual(
        markdown_to_blocks(md),
        ["First block", "Second block"],
    )

    def test_markdown_blocktype_heading1(self):
        md = "# This is a heading."

        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_markdown_blocktype_heading2(self):
            md = "## This is a heading."
    
            block_type = block_to_block_type(md)
            self.assertEqual(block_type, BlockType.HEADING)

    def test_markdown_heading2(self):
            md = "###### This is a heading."
    
            block_type = block_to_block_type(md)
            self.assertEqual(block_type, BlockType.HEADING)

    def test_markdown_blocktype_notheading(self):
            md = "###This is a NOT heading."
    
            block_type = block_to_block_type(md)
            self.assertNotEqual(block_type, BlockType.HEADING)

    def test_markdown_quote(self):
            md = "> This is a quote."
    
            block_type = block_to_block_type(md)
            self.assertEqual(block_type, BlockType.QUOTE)

    def test_markdown_quote2(self):
            md = ">This is a quote."
    
            block_type = block_to_block_type(md)
            self.assertEqual(block_type, BlockType.QUOTE)

    def test_markdown_code(self):
            md = "```This is code```"
    
            block_type = block_to_block_type(md)
            self.assertEqual(block_type, BlockType.CODE)

    def test_markdown_unorderedlist(self):
            md = """- This is the first item in an unordered list
- This is the second item
- This is the third item
            """
    
            block_type = block_to_block_type(md)
            self.assertEqual(block_type, BlockType.UNORDERED_LIST)
        
    
    def test_markdown_orderedlist(self):
            md = """1. This is the first item in an unordered list
2. This is the second item
3. This is the third item
            """
    
            block_type = block_to_block_type(md)
            self.assertEqual(block_type, BlockType.ORDERED_LIST)
            

    def test_markdown_orderedlist2(self):
            md = """1. This is the first item in an unordered list
3. This is wrong
6. This is wrong
            """
    
            block_type = block_to_block_type(md)
            self.assertNotEqual(block_type, BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()