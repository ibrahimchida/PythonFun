def flatten(exclude_non_alpha=True, default_case=True):
    file_to_read = open("contents.txt", "r")
    file_to_write_to = open("newcontents.txt", "w")
    file_contents = file_to_read.read().split()
    for word in file_contents:
        stripped_word = word.strip('1234567890')
        if exclude_non_alpha:
            if default_case:
                file_to_write_to.write(f"{stripped_word} \n")
            else:
                file_to_write_to.write(f"{stripped_word} \n".lower())
        else:
            file_to_write_to.write(f"{word} \n")


flatten(True, False)
