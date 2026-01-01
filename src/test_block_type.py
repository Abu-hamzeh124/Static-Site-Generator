import unittest
from block_type import block_to_block_type, BlockType

class Test(unittest.TestCase):  
    def test_block_to_block_paragraph(self):
        paragraph = '''
        hfgghdghgchdgcdc
        hdhgccdcgdcdcdhgcd
        '''
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)
    def test_block_to_block_heading(self):
        paragraph = "# vvvn"
        self.assertEqual(block_to_block_type(paragraph), BlockType.HEADING)        
    def test_block_to_block_unordered(self):
        paragraph = """   - cecedjcd
- sccndndn
- ccdcdcdcdc"""
        self.assertEqual(block_to_block_type(paragraph), BlockType.UNORDERED)
    def test_block_to_block_ordered(self):
        paragraph = """      1. cecedjcd
    2. sccndndn
   3. ccdcdcdcdc"""
        self.assertEqual(block_to_block_type(paragraph), BlockType.ORDERED)

if __name__ == "__main__":
    unittest.main()