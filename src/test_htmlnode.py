import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = { "href": "https://www.google.com", "target": "_blank" }
        node = HTMLNode("tag", "value", None, props)
        expected = " href=\"https://www.google.com\" target=\"_blank\""

        result = node.props_to_html()

        self.assertEqual(result, expected)

    def test_props_to_html_not_equals(self):
        props = { "href": "www.google.com", "target": "_blank" }
        node = HTMLNode("tag", "value", None, props)
        expected = " href=\"https://www.google.com\" target=\"_blank\""

        result = node.props_to_html()

        self.assertNotEqual(result, expected)

    def test_props_to_html_props_empty(self):
        props = {} 
        node = HTMLNode("tag", "value", None, props)
        expected = ""

        result = node.props_to_html()

        self.assertEqual(result, expected)

    def test_props_to_html_props_none(self):
        props = None
        node = HTMLNode("tag", "value", None, props)
        expected = "" 

        result = node.props_to_html() 

        self.assertEqual(result, expected)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()