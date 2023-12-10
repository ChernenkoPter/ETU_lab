import huffman as huf
from math import log


def partition_entropy(partition, words_to_counts):
    result = 0
    distribution = list(x[1] for x in words_to_counts)

    # get distribution of groups
    group_distribution = dict()
    for i in range(len(partition)):
        k = sum(partition[0:i])
        group_distribution[i] = sum(distribution[k:partition[i] + 1])

    group_nodes = group_distribution
    group_coding_prefixes = huf.get_huffman_coding(group_nodes)

    result = 0  # (длина префикса + длина символов в группе) * количество символов в группе
    for i in range(len(group_coding_prefixes)):
        result += (len(group_coding_prefixes[i]) + log(partition[i], 2)) * partition[i]
    return result
