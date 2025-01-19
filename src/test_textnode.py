import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_dif_textype(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_url(self):
        node1 = TextNode("Testing", TextType.BOLD)
        node2 = TextNode("Testing", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node1 = TextNode("Testing1", TextType.BOLD)
        node2 = TextNode("Testing2", TextType.BOLD)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
