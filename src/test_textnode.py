import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()