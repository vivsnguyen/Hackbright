"""Generate Markov text from text files."""

from random import choice
import string


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()


    return file




def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()


    chains = {}

    for i in range(len(words) - 1):
        chains[(words[i], words[i + 1])] = chains.get((words[i], words[i + 1]), [])
        try:
            chains[(words[i], words[i + 1])].append(words[i + 2])
        except:
            continue
    return chains


def make_text(chains_dict):
    """Return text from chains."""

    # link = list(chains_dict.keys())[0]
    # generated_sentence = [link[0], link[1]]
    upper_links = []

    for chain in chains.keys():
        if chain[0][0].isupper():
            upper_links.append(chain)

    link = choice(upper_links)
    generated_sentence = [link[0],link[1]]

    punctuation_keys = []
    # your code goes here
    for chain in chains.keys():
        if chain[1][-1] in string.punctuation and chain[1][-1] != ",":
            punctuation_keys.append(chain)     

    end_link = choice(punctuation_keys)

#loop starts
    while chains[link]:
        if link == end_link:
            break

        else:
            link = (link[1], choice(chains_dict[link]))
            generated_sentence.append(link[1])
                



    return " ".join(generated_sentence)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

make_chains("green-eggs.txt")

