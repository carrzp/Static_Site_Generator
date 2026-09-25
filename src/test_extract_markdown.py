import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is a link with a [link](https://www.google.com)")
        self.assertEqual([("link", "https://www.google.com")], matches)

    def test_multiple_images(self):
        text = "![cat](cat.png) and ![dog](dog.png)"
        self.assertEqual([("cat", "cat.png"), ("dog", "dog.png")], extract_markdown_images(text),)

    def test_multiple_links(self):
        text = "[docs](https://docs.example.com) then [home](/home)"
        self.assertEqual([("docs", "https://docs.example.com"), ("home", "/home")], extract_markdown_links(text),)

    def test_no_images(self):
        self.assertEqual([], extract_markdown_images("Just ordinary text."))

    def test_no_links(self):
        self.assertEqual([], extract_markdown_links("Just ordinary text."))

    def test_images_are_not_links(self):
        text = "![logo](logo.png) and [site](https://example.com)"
        self.assertEqual([("site", "https://example.com")],
            extract_markdown_links(text),)

if __name__ == "__main__":
    unittest.main()