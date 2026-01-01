import unittest
from extract_title import extract_title


class ExtractTitle_Test(unittest.TestCase):
    def test_h1_at_start(self):
        md = "# My Title"
        self.assertEqual(extract_title(md), "My Title")

    def test_no_h1_raises(self):
        md = "No headings here"
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertEqual(str(cm.exception), "NO h1 tags in this markdown")

    def test_preceding_text_multiple_hashes_returns_third_segment(self):
        md = "Intro # ignored # Actual Title"
        self.assertEqual(extract_title(md), "Actual Title")

    def test_preceding_text_single_hash_raises_index_error(self):
        md = "Intro text # OnlyOne"
        with self.assertRaises(IndexError):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
