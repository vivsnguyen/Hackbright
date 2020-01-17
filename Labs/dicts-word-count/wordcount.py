# put your code here.

def open_a_file(file_name):

    log_file = open(file_name)

    formatted_list_of_file = []

    for line in log_file:
        line = line.rstrip()
        line = line.split()
        formatted_list_of_file.extend(line)

    return formatted_list_of_file


def count_words(file_name):

    formatted_list_of_file = open_a_file(file_name)
    word_count_dict = {}

    for word in formatted_list_of_file:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict

def print_word_count(word_count_dict):

    for word in word_count_dict:
        print(word, word_count_dict[word])

print_word_count(count_words('test.txt'))
