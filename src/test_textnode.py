import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_texttype_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_texttype_uneq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url1(self):
        node = TextNode("This is a text node", TextType.LINK, url=None)
        node2 = TextNode("this is a text node", TextType.LINK, url="https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text_uneq1(self):
        node = TextNode("text node", TextType.TEXT, url=None)
        node2 = TextNode("text", TextType.ITALIC, url="https://www.boot.dev")
        self.assertNotEqual

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("a", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "a")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_img(self):
        node = TextNode("Google", TextType.IMAGE, url="https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "Google"})

if __name__ == "__main__":
    unittest.main()