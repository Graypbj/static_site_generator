import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "This is an HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("<p>", "This is an HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, node2.tag)

    def test_props(self):
        node = HTMLNode("<p>", "This is an HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),  " href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_eq_of_none(self):
        node = HTMLNode("<p>", "This is an HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("<p>", "This is an HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.children, node2.children)
    
    def test_repr(self):
        node = HTMLNode("<p>", "This is an HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), "tag=<p>, value=This is an HTML node, children=None, props={'href': 'https://www.google.com', 'target': '_blank'}")
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parent_no_tag(self):
        parent = ParentNode("div", [LeafNode("p", "Hello"), LeafNode(None, "World")])
        self.assertEqual(parent.to_html(), "<div><p>Hello</p>World</div>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
