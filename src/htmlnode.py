class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if(value is None):
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if(self.value is None):
            raise ValueError("LeafNode must have a value")
        if(self.tag is None):
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"