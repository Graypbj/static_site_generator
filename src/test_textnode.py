import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_uneq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_none_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
    
    def test_url_none_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.graysonbutcher.com")
        self.assertNotEqual(node, node2)
    
    def test_url_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.graysonbutcher.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.graysonbutcher.co")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.graysonbutcher.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.graysonbutcher.com)", repr(node)
            )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "This is an image"})
    
    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
