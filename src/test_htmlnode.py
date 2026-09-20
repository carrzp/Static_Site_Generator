from htmlnode import HTMLNode, LeafNode
import unittest

class Test_HTMLNode(unittest.TestCase):
    def test_props_to_html_eq1(self):
        node = HTMLNode("<p>", "string", [1, 2], {"href": "https://www.google.com"})
        actual = node.props_to_html()
        expected = f' href="https://www.google.com"'
        self.assertEqual(actual, expected)

    def test_props_to_html_eq2(self):
        node = HTMLNode("<a>", "string", [2, 3], {"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual, expected)

    def test_props_to_html_uneq(self):
        node = HTMLNode("<a>", "string", [2, 3], {"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = f' href="https://www.google.com" target="www.bootdev.com"'
        self.assertNotEqual

class Test_LeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is bold")
        self.assertEqual(node.to_html(), "<b>This is bold</b>")

    def test_leaf_to_html_uneq_ahref(self):
        node = LeafNode("a", "Click Me", {"href": "https://www.google.com"})
        self.assertNotEqual(node.to_html(), '<a href="https://www.google.com">Click Me')

    def test_leaf_to_html_eq_ahref(self):
            node = LeafNode("a","Click Me", {"href": "https://www.google.com"})
            self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me</a>')

if __name__ == "__main__":
    unittest.main() 