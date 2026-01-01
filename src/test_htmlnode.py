import unittest
from textnode import *
from text_to_html import text_node_to_html_node
from split_nodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_text(self):
       node = TextNode("This is a `code node`", TextType.TEXT)
       html_node = split_nodes_delimiter([node], '`', TextType.CODE)
       self.assertEqual(html_node, [
           TextNode("This is a ", TextType.TEXT, None),
           TextNode("code node", TextType.CODE, None)
       ])
    def test_multiple_bold(self):
        node = TextNode("**one** and **two**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(result, [
        TextNode("one", TextType.BOLD, None),
        TextNode(" and ", TextType.TEXT, None),
        TextNode("two", TextType.BOLD, None),
        ])

    
if __name__ == "__main__":
    unittest.main()