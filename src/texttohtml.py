from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    try:
        text_node.text_type
    except:
        raise Exception("Invalid text type")

    match text_node.text_type:
        case text_node.text_type.NORMAL:
            return LeafNode(None, text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("b", text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("i", text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("code", text_node.text)
        case text_node.text_type.LINKS:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case text_node.text_type.IMAGES:
            return LeafNode("img", None, {"src":text_node.url, "alt":text_node.text})
