import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_case(self):
        node = TextNode("Frontend sucks", TextType.ITALIC, "https://www.boot.dev/")   
        node2 = TextNode("Frontend sucks", TextType.BOLD, "https://www.boot.dev/")
        node3 = TextNode("Frontend sucks", TextType.BOLD, "https://www.boot.dev/")
        self.assertEqual(node2, node3)
        self.assertNotEqual(node, node3)


if __name__ == "__main__":
    unittest.main()