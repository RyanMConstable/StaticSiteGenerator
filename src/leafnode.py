from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value parameter cannot be None")
        
        if self.tag is None:
            return self.value

        open_tag = f"<{self.tag}>"
        close_tag = f"</{self.tag}>"
        if self.props is not None:
            open_tag = f"<{self.tag}{self.props_to_html()}>"
        return f"{open_tag}{self.value}{close_tag}"
