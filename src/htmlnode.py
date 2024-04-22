class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if(self.props is None):
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value='', props=None):
        if(value is None):
            # raise ValueError("LeafNode must have a value")
            value = ''
        super().__init__(tag, value, None, props)

    def to_html(self):
        # if(self.value is None):
        #     raise ValueError("LeafNode must have a value")
        if(self.tag is None):
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if(children is None):
            raise ValueError("ParentNode must have children")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if(self.tag is None):
            raise ValueError("ParentNode must have a tag")
        if(self.children is None):
            raise ValueError("ParentNode must have children")
        # print(f"<{self.tag} {self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>")
        return f"<{self.tag} {self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
    
    def __repr__(self):
        return super().__repr__()