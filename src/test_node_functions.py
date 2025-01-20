import unittest
from node_functions import *
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

    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_markdown_images_none(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_images(text), [])
        
    def test_markdown_links_none(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_links(text), [])

    def test_given_link_test(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL,)
        new_nodes = split_nodes_link([node])
        equal_list = [TextNode("This is text with a link ", TextType.NORMAL), TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"), TextNode(" and ", TextType.NORMAL), TextNode( "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),]
        self.assertEqual(new_nodes, equal_list)


    def test_given_image_test(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL,)
        new_nodes = split_nodes_image([node])
        equal_list = [TextNode("This is text with a link ", TextType.NORMAL), TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"), TextNode(" and ", TextType.NORMAL), TextNode( "to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),]
        self.assertEqual(new_nodes, equal_list)
