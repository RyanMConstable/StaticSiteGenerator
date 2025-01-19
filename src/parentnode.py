from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        if self.children is None or self.children == []:
            raise ValueError("Children cannot be None")

        return_string = ""
        for node in self.children:
            node_string = node.to_html()
            return_string += node_string

        open_tag = f"<{self.tag}>"
        close_tag = f"</{self.tag}>"
        if self.props:
            open_tag = f"<{self.tag}{self.props_to_html()}>"

        return f"{open_tag}{return_string}{close_tag}"
