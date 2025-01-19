import unittest

from main import text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode
from textnode import *

class TestNodetoHTML(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("Testing", TextType.NORMAL)
        self.assertEqual(f'{text_node_to_html_node(text_node)}', 'HTMLNode(None, Testing, None, None)')
