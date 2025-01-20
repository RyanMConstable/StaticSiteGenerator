import unittest

from leafnode import LeafNode

class LeaftNodeTest(unittest.TestCase):
    def test_value_error(self):
        node = LeafNode("Test", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_none_tag(self):
        node = LeafNode(None, "This is my text", None)
        self.assertEqual(node.to_html(), "This is my text")

    def test_tag_and_value(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_tag_value_and_props(self):
        node = LeafNode("a","Click me!", {"href":"https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
