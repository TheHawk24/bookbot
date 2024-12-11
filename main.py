def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    number_of_words = num_words(file_contents)
    count_char_occurence = count_char(file_contents)

    print_report(number_of_words, count_char_occurence)


def num_words(content):
    content_list = content.split()

    return len(content_list)


def count_char(content):

    char_count = {}

    for c in content:
        c = c.lower()
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    return char_count


def sort_on(char_count_dict):
    for key in char_count_dict:
        return char_count_dict[key]


def print_report(num_words, char_count):

    # create a list of only characters in the alphabet
    list_of_alpha = []
    for char in char_count:
        if char.isalpha():
            list_of_alpha.append({char: char_count[char]})

    # sort them out
    list_of_alpha.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for dic in list_of_alpha:
        for char in dic:
            print(f"The '{char}' character was found {dic[char]} times")

    print("--- End report ---")


if __name__ == '__main__':
    main()
