import math
import entropy
import huffman
import normalization
import matplotlib.pyplot as plt
import numpy as np


def create_plots(counts, words_num):
    # not useful plot
    plt.scatter(range(1, len(counts) + 1), counts)
    plt.show()

    # more info here
    plt.scatter(range(1, len(counts) + 1), list(math.log2(x) for x in counts))
    plt.show()

    # perfection
    bins = math.ceil(math.log2(max(counts))) + 1
    hist_list = [0] * bins
    for x in counts:
        x_ceil_log2 = math.ceil(math.log2(x))
        hist_list[x_ceil_log2] += 1
    hist_list_ceil_log2 = hist_list
    for i in range(0, len(hist_list_ceil_log2)):
        if hist_list_ceil_log2[i] != 0:
            hist_list_ceil_log2[i] = math.log2(hist_list_ceil_log2[i])
    plt.scatter(range(0, bins), hist_list_ceil_log2)
    plt.show()


if __name__ == "__main__":
    books = ['bible']
    for book in books:
        normalization.normalize(book)
        words_distrib, words_num = normalization.count_words_occurrences(book)
        counts = normalization.save_dict(book, words_distrib, words_num)
        create_plots(counts, words_num)
