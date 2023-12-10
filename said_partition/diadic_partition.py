def find_optimal_diadic_partition_group_sizes(words_to_counts, N_g_minmax, without_empty_elements=True):
    if N_g_minmax[0] < 1:
        N_g_minmax[0] = 1
    if without_empty_elements:
        N_g_minmax[0] = len(words_to_counts).bit_count()
    if N_g_minmax[1] > len(words_to_counts) - 1:
        N_g_minmax[1] = len(words_to_counts) - 1

    result = list()  # содержит множество пар "разбиение - средняя длина слова"

    # TODO реализовать поиск оптимального разбиения на диадические группы

    sorted(result.items(), key=lambda x: x[1], reverse=True)  # to get best partition into groups
    return result[0][0]
