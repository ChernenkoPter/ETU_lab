path_template = 'examples/{0}/{0}.txt'
normalized_path_template = 'examples/{0}/normalized_{0}.txt'
dict_path_template = 'examples/{0}/words_in_{0}.txt'


def normalize(text):
    f = open(path_template.format(text), "r")
    normalized_f = open(normalized_path_template.format(text), "w")

    c = f.read(1)
    while c:
        if c.isalpha() or c.isspace():
            normalized_f.write(c.lower())
        c = f.read(1)

    normalized_f.close()
    f.close()


def count_words_occurrences(text):
    f = open(normalized_path_template.format(text), "r")
    result = dict()
    words_in_text = 0
    for line in f:
        for word in line.split():
            words_in_text += 1
            result.update({word: result.get(word, 0) + 1})

    f.close()

    return sorted(result.items(), key=lambda x: x[1], reverse=True), words_in_text


def save_dict(text, words_distribution, word_num):
    f = open(dict_path_template.format(text), "w")

    message = "Book {} has {} words in it. In this file I'll save them in descending order.\n\n"
    f.write(message.format(text, word_num))

    list_count = list()
    for (word, count) in words_distribution:
        f.write("{} : {}\n".format(word, count))
        list_count.append(count)

    f.close()
    return list_count