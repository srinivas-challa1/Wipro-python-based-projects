from collections import defaultdict


def frequency_of_letters(name):
    count = defaultdict(int)
    for character in name:
        count[character] += 1
    res = [character+"-"+str(Count) for character, Count in count.items()]
    return("Frequency of Letters:"+",".join(res))
