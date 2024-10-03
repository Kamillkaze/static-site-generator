from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Node needs to have a tag")
        if self.children is None:
            raise ValueError("Node needs to have children")
        childrenHtml = ""
        for child in self.children:
            childrenHtml += child.to_html()
        return f"<{self.tag}>{childrenHtml}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.props})"