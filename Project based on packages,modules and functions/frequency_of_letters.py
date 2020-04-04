from collections import defaultdict

global name


def frequency_of_letters(name):
    count = defaultdict(int)
    for character in name:
        count[character] += 1
    res = [character+"-"+str(Count) for character, Count in count.items()]
    # return(res)
    return("Frequency of Letters:"+",".join(res))


'''
def Frequency(*list):
    # list = frequency_of_letters(name)
    return("Frequency of Letters:"+",".join(*list))
'''

'''
if __name__ == "__main__":
    print(Frequency(frequency_of_letters(input())))
'''
