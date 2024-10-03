from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(text_node):
        leafnode = LeafNode(None, None)
        if text_node.text_type == text_type_image:
            leafnode.tag = "img"
            leafnode.value = ""
            leafnode.props = { "src": f"{text_node.url}", "alt": f"{text_node.text}" }
        elif text_node.text_type == text_type_text:
            leafnode.tag = None
        elif text_node.text_type == text_type_bold:
            leafnode.tag = "b"
        elif text_node.text_type == text_type_italic:
            leafnode.tag = "i"
        elif text_node.text_type == text_type_code:
            leafnode.tag = "code"
        elif text_node.text_type == text_type_link:
            leafnode.tag = "a"
            leafnode.props = { "href": f"{text_node.url}" }
        else:
            raise Exception("type not supported") 
        
        leafnode.value = text_node.text

        return leafnode

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    