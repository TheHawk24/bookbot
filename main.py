def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    num_words(file_contents)


def num_words(content):
    content_list = content.split()

    return content_list


def count_char(content):
    pass


if __name__ == '__main__':
    main()
