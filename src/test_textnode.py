import unittest

from textnode import TextNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_different_text(self):
        node = TextNode("node 1", "italic")
        node2 = TextNode("node 2", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_different_text_type(self):
        node = TextNode("node 1", "italic")
        node2 = TextNode("node 1", "bold")
        self.assertNotEqual(node, node2)
    
    def test_eq_url_none_passed(self):
        node = TextNode("node 1", "bold", None)
        node2 = TextNode("node 1", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_url_different(self):
        node = TextNode("node 1", "bold", "url1")
        node2 = TextNode("node 1", "bold", "url2")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_type_text(self):
        text_node = TextNode("text", "text")
        expected = LeafNode(None, "text")

        result = text_node.text_node_to_html_node()

        self.assertEqual(result, expected)

    def test_text_node_to_html_node_type_text(self):
        text_node = TextNode("text", "bold")
        expected = LeafNode("b", "text")

        result = text_node.text_node_to_html_node()

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()