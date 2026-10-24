from main import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_title_extr1(self):
        markdown = "# This is a header"
        self.assertEqual(extract_title(markdown), "This is a header")

    def test_title_extr2(self):
        markdown = "## This is not a header"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_title_extr3(self):
            markdown = "### This is not a header"
            with self.assertRaises(Exception):
                extract_title(markdown)

    def test_title_extr4(self):
            markdown = "#### This is not a header"
            with self.assertRaises(Exception):
                extract_title(markdown)

    def test_title_extr5(self):
                markdown = "##### This is not a header"
                with self.assertRaises(Exception):
                    extract_title(markdown)

    def test_title_extr6(self):
                markdown = "###### This is not a header"
                with self.assertRaises(Exception):
                    extract_title(markdown)

    def test_title_extr7(self):
        markdown = "# This is a header #"
        self.assertEqual(extract_title(markdown), "This is a header #")

if __name__ == "__main__":
    unittest.main()