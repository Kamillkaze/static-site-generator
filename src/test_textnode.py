import unittest

from textnode import (
    TextNode,
    text_node_to_html_node
)
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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("text", "text")
        expected = LeafNode(None, "text")

        result = text_node_to_html_node(text_node)

        self.assertEqual(result, expected)
    
    def test_image(self):
        node = TextNode("This is an image", "image", "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_text_bold(self):
        text_node = TextNode("text", "bold")
        expected = LeafNode("b", "text")

        result = text_node_to_html_node(text_node)

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()