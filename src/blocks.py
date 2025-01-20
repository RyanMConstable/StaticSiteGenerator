


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

    return new_list

