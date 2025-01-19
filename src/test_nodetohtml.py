import unittest

from texttohtml import text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode
from textnode import *

class TestNodetoHTML(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("Testing", TextType.NORMAL)
        self.assertEqual(f'{text_node_to_html_node(text_node)}', 'HTMLNode(None, Testing, None, None)')

    def test_bold(self):
        text_node = TextNode("Testing", TextType.BOLD)
        self.assertEqual(f'{text_node_to_html_node(text_node)}', 'HTMLNode(b, Testing, None, None)')

    def test_italic(self):
        text_node = TextNode("Testing", TextType.ITALIC)
        self.assertEqual(f'{text_node_to_html_node(text_node)}', 'HTMLNode(i, Testing, None, None)')

    def test_code(self):
        text_node = TextNode("Testing", TextType.CODE)
        self.assertEqual(f'{text_node_to_html_node(text_node)}', 'HTMLNode(code, Testing, None, None)')

    def test_links(self):
        text_node = TextNode("Testing", TextType.LINKS, "https://www.google.com")
        self.assertEqual(f'{text_node_to_html_node(text_node)}', "HTMLNode(a, Testing, None, {'href': 'https://www.google.com'})")

    def test_images(self):
        text_node = TextNode("Testing", TextType.IMAGES, "https://test")
        self.assertEqual(f'{text_node_to_html_node(text_node)}', "HTMLNode(img, None, None, {'src': 'https://test', 'alt': 'Testing'})")
