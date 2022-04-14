import matplotlib.pyplot as plt
import math
import string


def open_file(file_name):
    word_dictionary = {}
    stop_words = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as",
                  "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can",
                  "could", "did", "do", "does", "doing", "done", "down", "during", "each", "few", "for", "from", "further",
                  "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
                  "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it",
                  "it's", "its", "itself", "just", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on",
                  "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she",
                  "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their",
                  "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
                  "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was",
                  "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where",
                  "where's", "which", "while", "who", "who's", "whom", "will", "why", "why's", "with", "would", "you",
                  "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]

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
                        if word not in stop_words:
                            if word not in word_dictionary:
                                word_dictionary[word] = 0
                            word_dictionary[word] += 1

    return(word_dictionary)


def jaccard_distance(main_dict, novel_dict, word_len):
    main_set = set()
    novel_set = set()

    for word in main_dict:
        if len(word) == word_len:
            main_set.add(word)

    for word in novel_dict:
        if len(word) == word_len:
            novel_set.add(word)

    similarity = len((main_set.intersection(novel_set))) / len((main_set.union(novel_set)))

    distance = 1 - similarity

    # print(f'main_set: {main_set} \n Novel_set: {novel_set}')
    print(distance)

def main(filename1, filename2, novel1, novel2):
    file1_dict = open_file(filename1)
    file2_dict = open_file(filename2)
    novel1_dict = open_file(novel1)
    novel2_dict = open_file(novel2)

    # DISTANCE FOR NOVEL 1
    # jaccard_distance(file1_dict, novel1_dict, 5)
    # jaccard_distance(file2_dict, novel1_dict, 5)
    # jaccard_distance(file1_dict, novel2_dict, 5)
    # jaccard_distance(file2_dict, novel2_dict, 5)
    #
    # jaccard_distance(file1_dict, novel1_dict, 6)
    # jaccard_distance(file2_dict, novel1_dict, 6)
    # jaccard_distance(file1_dict, novel2_dict, 6)
    # jaccard_distance(file2_dict, novel2_dict, 6)
    #
    # jaccard_distance(file1_dict, novel1_dict, 7)
    # jaccard_distance(file2_dict, novel1_dict, 7)
    # jaccard_distance(file1_dict, novel2_dict, 7)
    # jaccard_distance(file2_dict, novel2_dict, 7)
    #
    # jaccard_distance(file1_dict, novel1_dict, 8)
    # jaccard_distance(file2_dict, novel1_dict, 8)
    # jaccard_distance(file1_dict, novel2_dict, 8)
    # jaccard_distance(file2_dict, novel2_dict, 8)
    #
    # jaccard_distance(file1_dict, novel1_dict, 9)
    # jaccard_distance(file2_dict, novel1_dict, 9)
    # jaccard_distance(file1_dict, novel2_dict, 9)
    # jaccard_distance(file2_dict, novel2_dict, 9)
    #
    # jaccard_distance(file1_dict, novel1_dict, 10)
    # jaccard_distance(file2_dict, novel1_dict, 10)
    # jaccard_distance(file1_dict, novel2_dict, 10)
    # jaccard_distance(file2_dict, novel2_dict, 10)

    # open_file(filename2)

main('Jacob Kahn - Great_Expectations.txt', 'Jacob Kahn - Scarlet_Letter.txt', 'Novel1.txt', 'Novel2.txt')
