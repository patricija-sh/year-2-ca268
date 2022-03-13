def get_counts_dict(list):
    wordcount = {}
    for word in list:
        if len(word) not in wordcount:
            wordcount[len(word)] = 1
        else:
            wordcount[len(word)] += 1
    return wordcount
