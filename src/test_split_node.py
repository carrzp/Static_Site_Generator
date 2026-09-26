import unittest
from textnode import TextNode, TextType
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TextSplitNode(unittest.TestCase):
    def test_split_node_bold(self):
        node = TextNode("This is text with a **BOLD** word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node],"**", TextType.BOLD), [TextNode("This is text with a ", TextType.TEXT), TextNode("BOLD", TextType.BOLD), TextNode(" word", TextType.TEXT)])

    def test_split_node_italic(self):
            node = TextNode("This is text with a _italic_ word", TextType.TEXT)
            self.assertEqual(split_nodes_delimiter([node],"_", TextType.ITALIC), [TextNode("This is text with a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT)])

    def test_split_node_empty_str(self):
        node = TextNode("_Hello_ World", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node],"_", TextType.ITALIC), [TextNode("Hello", TextType.ITALIC), TextNode(" World", TextType.TEXT)])

    def test_split_node_non_text(self):
        node = TextNode("`Code`", TextType.CODE)
        self.assertEqual(split_nodes_delimiter([node],"`", TextType.CODE), [TextNode("`Code`", TextType.CODE)])

    def test_split_node_missing_delim(self):
            node = TextNode("**Hello World", TextType.TEXT)
            with self.assertRaises(Exception) as ctx:
                 split_nodes_delimiter([node],"**", TextType.BOLD)
            self.assertIn("Missing an opening or closing", str(ctx.exception))

    def test_split_node_two_delim(self):
            node = TextNode("**Hello** _World_", TextType.TEXT)
            first_split = split_nodes_delimiter([node],"**", TextType.BOLD)
            second_split = split_nodes_delimiter(first_split, "_", TextType.ITALIC)
            self.assertEqual(second_split, [TextNode("Hello", TextType.BOLD), TextNode(" ", TextType.TEXT), TextNode("World", TextType.ITALIC)])
                
    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
        
if __name__ == "__main__":
    unittest.main() 