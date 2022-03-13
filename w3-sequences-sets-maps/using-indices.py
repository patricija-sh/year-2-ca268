def get_counts(words):
    counts = [0] * 10
    for i in range(len(words)):
        counts[len(words[i])] += 1
    return counts
