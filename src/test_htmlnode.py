import unittest

from htmlnode import LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html(self):
        node = LeafNode("h1", "Frontend is not that impressing anymore!")
        node2 = LeafNode("h2", "Frontend in 2025 is like typing a link in a browser!")
        Parent_node = ParentNode("head", [node, node2])
        self.assertEqual(
            Parent_node.to_html(),
            "<head><h1>Frontend is not that impressing anymore!</h1><h2>Frontend in 2025 is like typing a link in a browser!</h2></head>",
        )    


if __name__ == "__main__":
    unittest.main()