from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is None!")

        if self.children == None:
            raise ValueError("No child provided!")

        r = f"<{self.tag}>"

        for child in self.children:
            r += child.to_html()

        r += f"</{self.tag}>"

        return r
