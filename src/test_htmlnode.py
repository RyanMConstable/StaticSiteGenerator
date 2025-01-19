import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        my_dict = {"href": "https://www.google.com", "target": "_blank",}
        my_node = HTMLNode(props = my_dict)
        self.assertEqual(my_node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        my_node = HTMLNode("a")
        self.assertEqual(f"{my_node}", "HTMLNode(a, None, None, None)")

    def test_repr2(self):
        my_node = HTMLNode()
        self.assertEqual(f"{my_node}", "HTMLNode(None, None, None, None)")

if __name__ == "__main__":
    unittest.main()
