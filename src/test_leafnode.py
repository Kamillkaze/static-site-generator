import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_children(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"

        result = node.to_html()

        self.assertEqual(result, expected)
    
    def test_to_html_tag_anchor(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = "<a href=\"https://www.google.com\">Click me!</a>"

        result = node.to_html()

        self.assertEqual(result, expected)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()