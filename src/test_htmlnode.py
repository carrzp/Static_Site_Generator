from htmlnode import HTMLNode, LeafNode, ParentNode
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

class Test_ChildNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_ordered_list(self):
        child_node4 = LeafNode("b", "grandchild")
        child_node3 = ParentNode("br", [child_node4])
        child_node2 = ParentNode("h1", [child_node3])
        child_node1 = ParentNode("span", [child_node2])
        parent_node = ParentNode("div", [child_node1])
        self.assertNotEqual(
        parent_node.to_html(), "<div><ul><li><b>bullet_point_one<b></li><li>bullet_point_two</li></ul></div>",)

    def test_to_html_ordered_list(self):
        child_node4 = LeafNode("b", "bullet_point_two")
        child_node3 = LeafNode("b", "bullet_point_one")
        child_node5 = ParentNode("li", [child_node4])
        child_node2 = ParentNode("li", [child_node3])
        child_node1 = ParentNode("ul", [child_node2, child_node5])
        parent_node = ParentNode("div", [child_node1])
        self.assertEqual(
        parent_node.to_html(), "<div><ul><li><b>bullet_point_one</b></li><li><b>bullet_point_two</b></li></ul></div>",)

if __name__ == "__main__":
    unittest.main() 