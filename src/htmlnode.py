class HTMLNode():
    def __init__(self, tag: str = None, value: str = None  , children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_str = ""
        if self.props == None:
            return ""
        for key, value in self.props.items():
            html_str += f' {key}="{value}"'
        return html_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str = None, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list = None, props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        child_html_node = ""
        if self.tag == None:
            raise ValueError("Missing a tag value")
        if self.children == None:
            raise ValueError("Missing a children list")
        if len(self.children) == 0:
            return f'<{self.tag}{self.props_to_html()}></{self.tag}>'
        for child in self.children:
            child_html_node += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{child_html_node}</{self.tag}>'