from node_functions import *

def markdown_to_blocks(markdown):
    list_lines = markdown.splitlines()
    new_list = []
    current_list = []
    for line in list_lines:
        if line == "":
            if current_list != []:
                new_list.append(current_list)
            current_list = []
            continue
        current_list.append(line)
    if current_list != []:
        new_list.append(current_list)

    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            new_list[i][j] = new_list[i][j].strip(" ")

    for i in range(len(new_list)):
        new_list[i] = "\n".join(new_list[i])

    return new_list



def block_to_block_type(block):
    lines = block.splitlines()

    if len(lines) == 1:
        is_heading = True 
        for item in lines[0].split(" ")[0]:
            if item != '#':
                is_heading = False
        if is_heading:
            return "heading"

    if block[0:3] == '```' and block[-3:] == '```' and len(block) >= 6:
        return "code"

    is_quote = True
    for item in lines:
        if item[0] != '>':
            is_quote = False
    if is_quote:
        return "quote"

    is_unordered_list = True
    for item in lines:
        if item[0] != '*':
            is_unordered_list = False
    if is_unordered_list:
        return "unordered_list"

    is_unordered_list = True
    for item in lines:
        if item[0] != '-':
            is_unordered_list = False
    if is_unordered_list:
        return "unordered_list"

    is_ordered_list = True
    num = 1
    for item in lines:
        if len(item) < 3:
            is_ordered_list = False
            break
        if item[0] != str(num) or item[1] != "." or item[2] != " ":
            is_ordered_list = False
            break
        num+=1 

    if is_ordered_list:
        return "ordered_list"

    return "paragraph"

txt = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""




list_blocks = markdown_to_blocks(txt)
for block in list_blocks:
    print(block_to_block_type(block))
    print(text_to_textnodes(block))
