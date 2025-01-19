import unittest

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class ParentNodeTest(unittest.TestCase):
    def test_given(self):
        children = [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")]
        node = ParentNode("p", children,)
        output_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), output_string)

    def test_no_children(self):
        node = ParentNode("b", [],)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "Bold text")],)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_nested_parent(self):
        children = [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")]
        parent = ParentNode("p", children,)

        new_children = [parent, LeafNode("b", "Bold text")]
        parent = ParentNode("p", new_children,)

        output_string = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b></p>"
        self.assertEqual(parent.to_html(), output_string)
