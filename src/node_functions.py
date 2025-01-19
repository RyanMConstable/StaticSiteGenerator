from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #old nodes is going to be a list of nodes
    #delimiter is going to be what we're looking for ie ** 

    if old_nodes == [] or old_nodes == None:
        return []

    new_nodes = []
    for node in old_nodes:
        split_list = node.text.split(delimiter)
        for i in range(len(split_list)):
            if split_list[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_list[i], TextType.NORMAL))
            else:
                new_nodes.append(TextNode(split_list[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
