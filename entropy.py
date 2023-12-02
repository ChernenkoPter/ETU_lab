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


# to test efficiency of functions tha compute entropy for random source
if __name__ == "__main__":
    x = int(input('Enter number of elements in list: '))
    start_create_list = datetime.datetime.now()
    test_list = create_test_list(x)
    end_create_list = datetime.datetime.now()

    start_compute_probabilities = datetime.datetime.now()
    elements_sum = sum(test_list)
    probs_list = list(elem/elements_sum for elem in test_list)
    end_compute_probabilities = datetime.datetime.now()

    start_entropy_1 = datetime.datetime.now()
    print('entropy 1 is {}'.format(entropy_1(probs_list, 2)))
    end_entropy_1 = datetime.datetime.now()

    start_entropy_2 = datetime.datetime.now()
    print('entropy 2 is {}'.format(entropy_2(test_list)))
    end_entropy_2 = datetime.datetime.now()

    print('{} to create list of {} elements'.format(end_create_list - start_create_list, x))
    print("{} to compute probabilities list".format(end_compute_probabilities - start_compute_probabilities))
    print('{} to compute entropy 1'.format(end_entropy_1 - start_entropy_1))
    print('{} to compute probabilities + entropy 1'.format(end_entropy_1 - start_compute_probabilities))
    print('{} to compute entropy 2 '.format(end_entropy_2 - start_entropy_2))

# Пример вывода программы:
# Enter number of elements in list: 100000000
# entropy 1 is 26.296808008152645
# entropy 2 is 26.29680800817682
# 0:01:47.858514 to create list of 100000000 elements
# 0:00:33.253834 to compute probabilities list
# 0:00:12.771133 to compute entropy 1
# 0:00:46.024975 to compute probabilities + entropy 1
# 0:00:33.210892 to compute entropy 2
