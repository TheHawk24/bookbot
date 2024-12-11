def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # num_words(file_contents)
    count_char(file_contents)


def num_words(content):
    content_list = content.split()

    return content_list


def count_char(content):

    char_count = {}

    for c in content:
        c = c.lower()
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    return char_count


if __name__ == '__main__':
    main()
