from partition import partition_entropy


def find_optimal_linear_partition_for_size(words_to_counts, N_g):
    result = list()
    # TODO реализовать вычисление оптимального разбиения
    return result


def find_optimal_linear_partition_group_sizes(words_to_counts, N_g_minmax):
    if N_g_minmax[0] < 1:
        N_g_minmax[0] = 1
    if N_g_minmax[1] > len(words_to_counts) - 1:
        N_g_minmax[1] = len(words_to_counts) - 1
    if N_g_minmax[0] > N_g_minmax[1]:
        print("Error: unexpected minimal and maximum group sizes")
        return None

    result = list()
    for N_g in range(N_g_minmax[0], N_g_minmax[1] + 1):  # create partition of N_g groups
        temp = find_optimal_linear_partition_for_size(words_to_counts, N_g)
        result.append((temp, partition_entropy(temp, words_to_counts)))

    sorted(result.items(), key=lambda x: x[1], reverse=True)  # to get best partition into groups
    return result[0]
