from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #old nodes is going to be a list of nodes
    #delimiter is going to be what we're looking for ie ** 

    if old_nodes == [] or old_nodes == None:
        return []

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

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
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    if old_nodes == [] or old_nodes is None:
        return new_nodes

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        text = node.text
        extracted = extract_markdown_images(node.text)
        
        if extracted == []:
            continue

        for extract in extracted:
            text = text.split(f"![{extract[0]}]({extract[1]})")
            new_nodes.append(TextNode(text[0], TextType.NORMAL))
            new_nodes.append(TextNode(extract[0], TextType.IMAGES, extract[1]))
            text = text[1:]
            text = "".join(text)

        if text != [] and text != None and text != "":
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    if old_nodes == [] or old_nodes is None:
        return new_nodes

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        text = node.text
        extracted = extract_markdown_links(node.text)
        
        if extracted == []:
            continue

        for extract in extracted:
            text = text.split(f"[{extract[0]}]({extract[1]})")
            new_nodes.append(TextNode(text[0], TextType.NORMAL))
            new_nodes.append(TextNode(extract[0], TextType.LINKS, extract[1]))
            text = text[1:]
            text = "".join(text)

        if text != [] and text != None and text != "":
            new_nodes.append(TextNode(text, TextType.NORMAL))



    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    print(node)
    nodes = split_nodes_link([node])
    print(nodes)
    nodes = split_nodes_image(nodes)
    print(nodes)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    print(nodes)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    print(nodes)
    nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
    return nodes

print(text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))
