import unittest
from node_functions import split_nodes_delimiter
from textnode import *

class NodeFunctionsTest(unittest.TestCase):
    def test_given_case(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.NORMAL), TextNode("code block", TextType.CODE), TextNode(" word", TextType.NORMAL), ])

    def test_start_delimiter(self):
        node = TextNode("`Code block` is the area of concern", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Code block", TextType.CODE), TextNode(" is the area of concern", TextType.NORMAL), ])

    def test_end_delimiter(self):
        node = TextNode("Ending del `code`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Ending del ", TextType.NORMAL), TextNode("code", TextType.CODE), ])

    def test_double_msg(self):
        node = TextNode("`Start` and `end`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Start", TextType.CODE), TextNode(" and ", TextType.NORMAL), TextNode("end", TextType.CODE), ])
