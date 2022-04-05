import matplotlib.pyplot as plt
import math
import string


def open_file(file_name):
    word_dictionary = {}

    punctuation = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~”“'

    with open(file_name) as file:
        for row in file:
            row = row.split()
            row_len = len(row)

            if row_len >= 1:
                # EACH CHAPTER
                if row[0].lower() == 'chapter':
                    pass

                else:
                    for word in row:
                        word = word.lower()
                        word = word.translate(str.maketrans("", "", punctuation))
                        if word not in word_dictionary:
                            word_dictionary[word] = 0
                        word_dictionary[word] += 1

    print(word_dictionary)



def main(filename1, filename2):
    # open_file(filename1)
    open_file(filename2)


main('Jacob Kahn - Great_Expectations.txt', 'Jacob Kahn - Scarlet_Letter.txt')
