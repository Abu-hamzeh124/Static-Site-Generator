import unittest
from extract_markdown import markdown_to_blocks

class Markdown_Test(unittest.TestCase):
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
    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [""])
    def test_markdown_to_blocks_no_paragraphs(self):
        md = "This is a single paragraph with no breaks."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph with no breaks."])       
    def test_markdown_to_blocks_multiple_breaks(self):
        md = """
          This is a paragraph.

    ```This is another paragraph.```  
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(                                       
            blocks,
            [
                "This is a paragraph.",
                "```This is another paragraph.```",
            ],
        )

    def test_markdown_to_blocks_whitespace(self):
        md = "   This is a paragraph with leading and trailing whitespace.    "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph with leading and trailing whitespace."])

if __name__ == "__main__":
    unittest.main()        