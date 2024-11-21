class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props != None:
            final_prop_string = ""
            keys = self.props.keys()
            for key in keys:
                final_prop_string += (f" {key}=\"{self.props[key]}\"")
            return final_prop_string
        return ""
    
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag")
        if not self.children:
            raise ValueError("Invalid HTML: no children")
        final_html = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            final_html += child.to_html()
        return final_html + f"</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
