from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)


    def to_html(self):
        if self.value == None:
            raise ValueError("Value is None!")

        if self.tag == None:
            return self.value

        r = f"<{self.tag}"

        if self.props != None:
            for prop in self.props:
                r += f" {prop}=\"{self.props[prop]}\""

        r += f">{self.value}</{self.tag}>"

        return r


    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props}\n"
