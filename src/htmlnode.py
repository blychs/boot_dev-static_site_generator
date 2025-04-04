class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_text = ""
        if self.props is not None:
            for key, value in self.props.items():
                html_text += f' {key}="{value}"'
        return html_text

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag}, value={self.value}, "
                f"children={self.children}, props={self.props}")


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf must have value")
        if self.tag is None:
            return self.value
        html_start_tag = f"<{self.tag}{self.props_to_html()}" + ">"
        html_end_tag = f"</{self.tag}>"
        return f"{html_start_tag}{self.value}{html_end_tag}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is None")
        if self.children is None:
            raise ValueError("ParentNode without children")
        html = ""
        for child in self.children:
            html += child.to_html()
        html_start_tag = f"<{self.tag}{self.props_to_html()}" + ">"
        html_end_tag = f"</{self.tag}>"
        return html_start_tag + html + html_end_tag
