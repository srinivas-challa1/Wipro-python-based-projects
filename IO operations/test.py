fname = input()
file = open(fname, "r")
words = [word for line in file for word in line.split()]
Meeting_place = max(words, key=words.count)+" Street"
print(Meeting_place)
