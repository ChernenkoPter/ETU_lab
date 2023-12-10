from normalization import count_words_occurrences
from linear_partition import find_optimal_linear_partition_group_sizes
from diadic_partition import find_optimal_diadic_partition_group_sizes


def optimal_partition(words_to_counts, is_linear):
    if is_linear:  # find groups for optimal partitions
        group_sizes = find_optimal_linear_partition_group_sizes(words_to_counts, [1, len(words_count)])
    else:
        group_sizes = find_optimal_diadic_partition_group_sizes(words_to_counts, [1, len(words_count)])

    it = iter(words_to_counts)
    return [[next(it) for _ in range(size)] for size in group_sizes]  # break words_to_counts into these groups


if __name__ == "__main__":  # example
    book = "bible"
    words, words_count = count_words_occurrences(book)
