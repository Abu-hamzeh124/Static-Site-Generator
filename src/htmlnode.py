class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return None
        result = ""
        for k, v in self.props.items():
            result+= f' {k}="{v}"'
        return result    
    def __repr__(self):
        print(self.props) 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props) 
    def to_html(self):   
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            result = ""
            if self.props is not None:
                result += f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                 result += f"<{self.tag}>{self.value}</{self.tag}>" 
            return result
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag Missing")
        if self.children is None:
            raise ValueError("Children Missing")
        else:
            result = ""
            for child in self.children: 
                result += child.to_html()
            if self.props is None:
                final_result = f"<{self.tag}>{result}</{self.tag}>"
            else:
                final_result = f"<{self.tag} {self.props_to_html()}>{result}</{self.tag}>"    
            return final_result    

                 

    
