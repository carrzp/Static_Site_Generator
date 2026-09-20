from htmlnode import HTMLNode
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

if __name__ == "__main__":
    unittest.main() 