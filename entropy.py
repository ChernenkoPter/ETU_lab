import numpy as np
from math import log, e, ceil
import datetime
import os


# compute entropy from probabilities of symbols
def entropy_1(probabilities, base):
    ent = 0.

    # Compute entropy
    base = e if base is None else base
    for i in probabilities:
        ent -= i * log(i, base)

    return ent


def entropy_of_text(labels, base=None):
    """ Computes entropy of label distribution. """

    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    value, counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels

    return entropy_1(probs, base)


# compute entropy from number of occurrences of symbols
def entropy_2(symbols_distrib):
    alphabet_size = sum(symbols_distrib)
    ent = log(alphabet_size, 2)
    sum_nlogn = 0
    for d in symbols_distrib:
        sum_nlogn += d * log(d, 2)
    return ent - sum_nlogn/alphabet_size


def create_test_list(list_len):
    nums_sizes = ceil(log(x, 256))
    res = list(int.from_bytes(os.urandom(nums_sizes), "big") + 1 for i in range(0, x))
    return sorted(res, reverse=True)


if __name__ == "__main__":
    x = int(input('Enter number of elements in list: '))
    start = datetime.datetime.now()
    test_list = create_test_list(x)
    end = datetime.datetime.now()
    print('{} seconds to create list of {} elements'.format(end - start, x))

    start = datetime.datetime.now()
    end = datetime.datetime.now()
    print('entropy 1 took {} to compute for {} elements'.format(end - start, x))
    elements_sum = sum(test_list)
    probs_list = list(elem/elements_sum for elem in test_list)
    print('entropy 1 is {}'.format(entropy_1(probs_list, 2)))

    start_entropy_2 = datetime.datetime.now()
    print('entropy 2 is {}'.format(entropy_2(test_list)))
    end = datetime.datetime.now()
    print('entropy 2 took {} to compute for {} elements'.format(end - start, x))
