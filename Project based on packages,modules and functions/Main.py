from collections import defaultdict


def vowelCount(name):
    vowels = "aeiou"
    vc = 0
    for character in name:
        if character.lower() in vowels:
            vc += 1
        else:
            continue
    return("No of vowels:{}".format(vc))


def frequency_of_letters(name):
    count = defaultdict(int)
    for character in name:
        count[character] += 1
    res = [character+"-"+str(Count) for character, Count in count.items()]
    return("Frequency of Letters:"+",".join(res))


def ispalindrome(name):
    if(name == name[::-1]):
        return("Yes it is palindrome")
    else:
        return("No,it is not a palindrome")
